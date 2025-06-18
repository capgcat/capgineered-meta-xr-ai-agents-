
from google.adk import Agent
# from .tools import toolbox_tools # Old import
from .tools import  toolbox_tools
from .prompt import DATA_IMPORT_PROMPT
from machine_sensors_ai_agents.sub_agents.rag_agent.agent import rag_agent
from google.adk.tools.agent_tool import AgentTool

MODEL = "gemini-2.0-flash"

data_import_agent = Agent(
    model=MODEL,
    name="data_import_agent",
    instruction=DATA_IMPORT_PROMPT,
    output_key="data_import_agent",
    tools=[*toolbox_tools, AgentTool(agent=rag_agent)], # Use the new list of ADK tools
)