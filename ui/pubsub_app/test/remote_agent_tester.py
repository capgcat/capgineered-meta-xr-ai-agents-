import os
import json
from dotenv import load_dotenv
import vertexai
from vertexai import agent_engines

def main():
    """
    Initializes Vertex AI, connects to a remote agent, and sends a query.
    """

    print("Starting remote agent tester...")
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION")
    staging_bucket_name = os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")
    # In your .env it's AGENT_RESOURCE_ID, ensure this is the full resource name
    agent_engine_id = os.environ["AGENT_ENGINE_ID"]

    required_vars = {
        "GOOGLE_CLOUD_PROJECT": project_id,
        "GOOGLE_CLOUD_LOCATION": location,
        "GOOGLE_CLOUD_STORAGE_BUCKET": staging_bucket_name,
        "AGENT_ENGINE_ID": agent_engine_id
    }

    missing_vars = [name for name, value in required_vars.items() if not value]
    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
        print("Please ensure your .env file is correctly set up in the ui/pubsub_app directory.")
        return

    # Defensively strip any trailing slash from the agent resource name
    if agent_engine_id:
        agent_engine_id = agent_engine_id.rstrip('/')

    print(f"Using Project ID: {project_id}")
    print(f"Using Location: {location}")
    print(f"Using Staging Bucket: gs://{staging_bucket_name}")
    print(f"Attempting to connect to Agent: {agent_engine_id}")

    try:
        vertexai.init(
            project=project_id,
            location=location,
            staging_bucket=f"gs://{staging_bucket_name}",
        )
        print("Vertex AI initialized successfully.")

        user_id="user"
        agent = agent_engines.get(agent_engine_id)
        session = agent.create_session(user_id=user_id)
        print("Type 'quit' to exit.")
        #while True:
        #    user_input = input("Input: ")
        #    if user_input == "quit":
        #        break
        user_input = "What is the current status of the sensors?"
        for event in agent.stream_query(
            user_id=user_id, session_id=session["id"], message=user_input
        ):
            if "content" in event:
                if "parts" in event["content"]:
                    parts = event["content"]["parts"]
                    for part in parts:
                        if "text" in part:
                            text_part = part["text"]
                            print(f"Response: {text_part}")

        agent.delete_session(user_id=user_id, session_id=session["id"])

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()