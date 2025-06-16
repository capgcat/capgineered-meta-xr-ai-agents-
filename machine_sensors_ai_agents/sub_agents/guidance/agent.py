from google.adk.agents import Agent

from .prompt import GUIDANCE_AGENT_INSTRUCTION
from google.adk.tools.tool_context import ToolContext
from typing import Optional, List, Dict
from .tools import toolbox_tools
from machine_sensors_ai_agents.sub_agents.rag_agent_guidance.agent import rag_agent_guidance

guidance_agent = Agent(
    name="guidance_agent",
    model="gemini-2.0-flash",
    description="Provides step-by-step assistance and diagnostic guidance to technicians for resolving machine issues based on predicted maintenance needs and detected anomalies.",
    instruction=GUIDANCE_AGENT_INSTRUCTION,
    sub_agents=[rag_agent_guidance],  # Include the rag_agent_guidance for RAG capabilities
    tools=[*toolbox_tools]   
)