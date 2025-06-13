from google.adk import Agent
from .tools import toolbox_tools
from .prompt import BIGQUERY_AGENT_INSTRUCTION


MODEL = "gemini-2.0-flash"


root_agent = Agent(
    model=MODEL,
    name="bigquery_agent",
    instruction=BIGQUERY_AGENT_INSTRUCTION,
    output_key="bigquery_agent",
    tools=[*toolbox_tools],
)