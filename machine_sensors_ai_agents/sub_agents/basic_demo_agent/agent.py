from google.adk.agents import Agent

from .prompt import BASIC_DEMO_AGENT_INSTRUCTION
from .tools import count_characters

basic_demo_agent = Agent(
    name="adk_short_bot",
    model="gemini-2.0-flash",
    description="A bot that shortens messages while maintaining their core meaning",
    instruction=BASIC_DEMO_AGENT_INSTRUCTION,
    tools=[count_characters],
)