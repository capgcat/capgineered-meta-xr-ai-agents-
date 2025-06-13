from google.adk.agents import Agent

from .prompt import ANOMALY_AGENT_INSTRUCTION
from machine_sensors_ai_agents.sub_agents.bigquery.agent import bigquery_agent

anomaly_agent = Agent(
    name="anomaly_agent",
    model="gemini-2.0-flash",
    description="Identifies abnormal patterns and deviations in real-time industrial sensor data.",
    instruction=ANOMALY_AGENT_INSTRUCTION,
    sub_agents=[bigquery_agent],
)