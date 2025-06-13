from google.adk.agents import Agent

from .prompt import PREDICTION_MAINTAINENCE_AGENT_INSTRUCTION

prediction_maintainence_agent = Agent(
    name="prediction_maintainence_agent",
    model="gemini-2.0-flash",
    description="Analyzes anomaly alerts and historical data to forecast potential equipment failures and recommend proactive maintenance.",
    instruction=PREDICTION_MAINTAINENCE_AGENT_INSTRUCTION,
)