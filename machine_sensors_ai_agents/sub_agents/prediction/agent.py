from google.adk.agents import Agent

from .prompt import PREDICTION_MAINTAINENCE_AGENT_INSTRUCTION
from .tools import toolbox_tools  # Import the updated toolbox tools
from machine_sensors_ai_agents.sub_agents.rag_agent.agent import rag_agent
from google.adk.tools.agent_tool import AgentTool

prediction_maintainence_agent = Agent(
    name="prediction_maintainence_agent",
    model="gemini-2.0-flash",
    description="Analyzes anomaly alerts and historical data to forecast potential equipment failures and recommend proactive maintenance.",
    instruction=PREDICTION_MAINTAINENCE_AGENT_INSTRUCTION,
    tools=[*toolbox_tools, AgentTool(agent=rag_agent)], 
)