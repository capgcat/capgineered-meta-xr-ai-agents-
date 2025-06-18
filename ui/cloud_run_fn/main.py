import base64
import functions_framework
import requests # Make sure to add 'requests' to your requirements.txt
import json
import os

# Environment variable for the agent URL, or use a default
AGENT_APP_URL = os.environ.get("AGENT_APP_URL", "https://machine-sensors-ai-agents-73933154165.us-central1.run.app")

# Configuration for the agent
APP_NAME = "machine_sensors_ai_agents" # As per your cURL example
USER_ID = "api_user"       # As per your cURL example
SESSION_ID = "api_session_1" # As per your cURL example, consider making this dynamic if needed

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def pubsub(cloud_event):
    print("Cloud event received.")
    
    try:
        # 1. Decode the Pub/Sub message
        pubsub_message_data = base64.b64decode(cloud_event.data["message"]["data"])
        print(f"Decoded Pub/Sub message data: {pubsub_message_data}")
        
        # Assuming the Pub/Sub message is a JSON string containing the text for the agent
        # If it's just plain text, adjust accordingly
        try:
            message_payload = json.loads(pubsub_message_data)
            agent_input_text = message_payload.get("text", "Default message: Hello?")
        except json.JSONDecodeError:
            agent_input_text = pubsub_message_data.decode('utf-8') # Fallback if not JSON
            if not agent_input_text.strip(): # Handle empty message
                 agent_input_text = "Default message: Hello?"
        except Exception as e:
            print(f"Error processing Pub/Sub message content: {e}")
            agent_input_text = "Error processing input: Hello?"


        # 2. Create Session
        session_url = f"{AGENT_APP_URL}/apps/{APP_NAME}/users/{USER_ID}/sessions/{SESSION_ID}"
        session_payload = {"state": {}} # Optional initial state
        headers = {"Content-Type": "application/json"}

        print(f"Creating session at: {session_url}")
        session_response = requests.post(session_url, json=session_payload, headers=headers)
        
        if session_response.status_code == 200 or session_response.status_code == 201:
            print(f"Session created/updated successfully: {session_response.json()}")
        else:
            print(f"Error creating session: {session_response.status_code} - {session_response.text}")
            # Optionally, you might want to stop here if session creation fails
            # return


        # 3. Run Agent (Send Message)
        run_agent_url = f"{AGENT_APP_URL}/run_sse"
        agent_payload = {
            "app_name": APP_NAME,
            "user_id": USER_ID,
            "session_id": SESSION_ID,
            "new_message": {
                "role": "user",
                "parts": [{"text": agent_input_text}]
            },
            "streaming": False # As per your cURL example
        }

        print(f"Running agent at: {run_agent_url} with payload: {json.dumps(agent_payload)}")
        agent_response = requests.post(run_agent_url, json=agent_payload, headers=headers)

        if agent_response.status_code == 200:
            # For run_sse, the response might be streamed. 
            # If streaming=False, it should be a complete JSON.
            # If streaming=True, you'd handle Server-Sent Events here.
            print(f"Agent run successfully. Response:")
            # Assuming non-streaming, the response content will be JSON
            # For SSE, you would iterate over agent_response.iter_lines()
            try:
                print(agent_response.json())
            except requests.exceptions.JSONDecodeError:
                print(agent_response.text) # Print raw text if not JSON
        else:
            print(f"Error running agent: {agent_response.status_code} - {agent_response.text}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
