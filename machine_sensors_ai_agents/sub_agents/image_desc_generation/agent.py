
from google.adk import Agent


from .prompt import IMAGE_DESC_GENERATATION_PROMPT
from .tools import gcs_reader_tool, gemini_describer_tool

MODEL = "gemini-2.0-flash"


image_desc_generation_agent = Agent(
    model=MODEL,
    name="image_desc_generation_agent",
    instruction=IMAGE_DESC_GENERATATION_PROMPT,
    tools=[gcs_reader_tool, gemini_describer_tool], # Register your tools with the agent
  )