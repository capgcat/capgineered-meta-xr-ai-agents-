from datetime import datetime
import os

from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def decode_pubsub_message(message: dict) -> str:
    """
    Decodes a Pub/Sub message and returns the data as a string.
    """
    if not message or "data" not in message:
        return "No data found in the Pub/Sub message."

    # Decode the base64-encoded data
    import base64
    decoded_data = base64.b64decode(message["data"]).decode("utf-8")
    
    return decoded_data