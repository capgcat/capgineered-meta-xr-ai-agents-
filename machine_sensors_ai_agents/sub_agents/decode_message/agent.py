
from google.adk import Agent
# from .tools import toolbox_tools # Old import
from .tools import  decode_pubsub_message


MODEL = "gemini-2.0-flash"

decode_message_agent = Agent(
    model=MODEL,
    name="decode_message_agent",
    instruction="Decode a Pub/Sub data message and return the data as a json string.",
    description=(
        'Decode a Pub/Sub data message and return the data as a json string. '
        'This agent is responsible for decoding messages from Google Cloud Pub/Sub, '
        'which are typically base64-encoded strings containing JSON data.'
    ),
    output_key="decode_message_agent",
    tools=[decode_pubsub_message], # Use the new list of ADK tools
)