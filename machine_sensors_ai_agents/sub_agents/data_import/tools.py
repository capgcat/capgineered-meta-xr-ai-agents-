from datetime import datetime
import os
from functools import partial

from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from toolbox_core import ToolboxSyncClient
from google.adk.tools import FunctionTool

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ----- Example of Google Cloud Tools (MCP Toolbox for Databases) -----
TOOLBOX_URL = os.getenv("MCP_TOOLBOX_URL_BQ", "http://127.0.0.1:5000")

toolbox = ToolboxSyncClient(TOOLBOX_URL)
toolbox_tools = toolbox.load_toolset("iot_device_toolset")