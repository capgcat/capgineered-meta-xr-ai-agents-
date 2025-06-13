import base64
import json
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, HTTPException
from fastapi.concurrency import run_in_threadpool
from dotenv import load_dotenv
import vertexai
from vertexai import agent_engines

load_dotenv()

# Configuration - these will be loaded from environment variables
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
STAGING_BUCKET_NAME = os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")
# AGENT_ENGINE_ID is the full resource name, e.g., projects/.../reasoningEngines/...
AGENT_ENGINE_ID = os.getenv("AGENT_ENGINE_ID") # Matching your .env and current script

# Global variable to store the agent client
_agent_client = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global _agent_client
    print("Application startup...")

    required_vars = {
        "GOOGLE_CLOUD_PROJECT": PROJECT_ID,
        "GOOGLE_CLOUD_LOCATION": LOCATION,
        "GOOGLE_CLOUD_STORAGE_BUCKET": STAGING_BUCKET_NAME,
        "AGENT_ENGINE_ID": AGENT_ENGINE_ID
    }
    missing_vars = [name for name, value in required_vars.items() if not value]
    if missing_vars:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")

    print(f"PROJECT_ID: {PROJECT_ID}")
    print(f"LOCATION: {LOCATION}")
    print(f"STAGING_BUCKET_NAME: {STAGING_BUCKET_NAME}")
    print(f"AGENT_ENGINE_ID: {AGENT_ENGINE_ID}")

    try:
        vertexai.init(
            project=PROJECT_ID,
            location=LOCATION,
            staging_bucket=f"gs://{STAGING_BUCKET_NAME}",
        )
        print("Vertex AI initialized successfully.")

        print(f"Getting remote agent: {AGENT_ENGINE_ID}")
        _agent_client = agent_engines.get(AGENT_ENGINE_ID) # This is a synchronous call
        if not _agent_client:
            raise RuntimeError(f"Failed to get agent client for {AGENT_ENGINE_ID}.")
        print(f"Successfully connected to agent: {_agent_client.name}")

        yield # Application is ready
    except Exception as e:
        print(f"Error during Vertex AI initialization or agent connection: {e}")
        # Re-raise to prevent app from starting in a bad state
        raise RuntimeError(f"Startup failed due to Vertex AI/Agent Engine error: {e}")
    finally:
        print("Application shutdown...")
        # Add any cleanup code here if needed

app = FastAPI(lifespan=lifespan)

@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World PubSub GET!"}

@app.post("/", tags=["root"])
async def post_root(request: Request):
    global _agent_client
    if not _agent_client:
        raise HTTPException(status_code=503, detail="Agent client not initialized. Check server logs.")

    envelope = await request.json()
    if not envelope or "message" not in envelope:
        raise HTTPException(status_code=400, detail="Invalid Pub/Sub message format")

    pubsub_message = envelope["message"]

    if "data" in pubsub_message:
        try:
            decoded_data = base64.b64decode(pubsub_message["data"]).decode("utf-8")
            message_json = json.loads(decoded_data)
            print(f"Received message: {message_json}")
            
            # The input for your agent is the decoded JSON payload
            agent_input = decoded_data 
            print(f"Querying agent with input: {decoded_data}")

            agent_input = "Test calling the agent"

            user_id="user"
            session = _agent_client.create_session(user_id=user_id)


            for event in _agent_client.stream_query(
                user_id=user_id, session_id=session["id"], message=agent_input
            ):
                if "content" in event:
                    if "parts" in event["content"]:
                        parts = event["content"]["parts"]
                        for part in parts:
                            if "text" in part:
                                text_part = part["text"]
                                print(f"Response: {text_part}")

            # agent.query() is synchronous, run in threadpool
            _agent_client.delete_session(user_id=user_id, session_id=session["id"])
            print(f"Agent response: {text_part}")

            return {"received_message": message_json, "agent_response": text_part}
        except (json.JSONDecodeError, UnicodeDecodeError, base64.binascii.Error) as e:
            raise HTTPException(status_code=400, detail=f"Error decoding Pub/Sub message data: {e}")
        except Exception as e:
            # Catch other exceptions, including potential errors from the agent call
            raise HTTPException(status_code=500, detail=f"Error processing message or calling agent: {e}")
    return {"message": "Empty Pub/Sub message received"}