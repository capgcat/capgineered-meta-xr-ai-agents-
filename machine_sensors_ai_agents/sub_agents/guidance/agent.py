from google.adk.agents import Agent

from .prompt import GUIDANCE_AGENT_INSTRUCTION

guidance_agent = Agent(
    name="guidance_agent",
    model="gemini-2.0-flash",
    description="Provides step-by-step assistance and diagnostic guidance to technicians for resolving machine issues based on predicted maintenance needs and detected anomalies.",
    instruction=GUIDANCE_AGENT_INSTRUCTION,
)