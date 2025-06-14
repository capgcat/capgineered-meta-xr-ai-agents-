from google.adk.agents import Agent

from .prompt import ANOMALY_AGENT_INSTRUCTION
from .tools import toolbox_tools  # Import the updated toolbox tools
from machine_sensors_ai_agents.sub_agents.rag_agent.agent import rag_agent

anomaly_agent = Agent(
    name="anomaly_agent",
    model="gemini-2.0-flash",
    description="Identifies abnormal patterns and deviations in real-time industrial sensor data.",
    instruction=ANOMALY_AGENT_INSTRUCTION,
    sub_agents=[rag_agent],  # Include the rag_agent for RAG capabilities
    tools=[*toolbox_tools], # Use the new list of ADK tools
)