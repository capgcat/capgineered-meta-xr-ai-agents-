from google.adk.agents import Agent

from .prompt import ANOMALY_AGENT_INSTRUCTION
from .tools import toolbox_tools  # Import the updated toolbox tools
from machine_sensors_ai_agents.sub_agents.rag_agent.agent import rag_agent
from machine_sensors_ai_agents.sub_agents.notification.agent import notification_agent
from google.adk.tools.agent_tool import AgentTool

anomaly_agent = Agent(
    name="anomaly_agent",
    model="gemini-2.0-flash",
    description="Identifies abnormal patterns and deviations in real-time industrial sensor data.",
    instruction=ANOMALY_AGENT_INSTRUCTION,
    tools=[*toolbox_tools, AgentTool(agent=rag_agent),AgentTool(agent=notification_agent)], # Use the new list of ADK tools
)