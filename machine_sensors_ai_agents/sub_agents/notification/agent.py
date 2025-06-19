from google.adk.agents import Agent
from .prompt import NOTIFICATION_AGENT_INSTRUCTION
from google.adk.tools.tool_context import ToolContext
from typing import Optional, List, Dict
from .tools import toolbox_tools, publishDeviceNotification, createIncidentBridge
from machine_sensors_ai_agents.sub_agents.rag_agent.agent import rag_agent
from google.adk.tools.agent_tool import AgentTool
from jira import JIRA
from dotenv import load_dotenv
import os

# Load environment variables
JIRA_URL="https://capgineered-agents-machine.atlassian.net/"
EMAIL="sandeep.kudterkar@capgemini.com"
API_TOKEN= "ATATT3xFfGF0ajAk32zbfjcL9JNu0UyRdJtzn5dwRfhKdZWVkPBbsPR7cEA8NG8d0AVUiUgdVfJ_g6uCOpfyu_0GyNPWAEtGb13s4T_eKzGo9RoC7rHI2mUX-b_RS0NBLPHkw5rLY4t0ajfHznEPY5Fj6tCEuxN-dAKkq3V6a7-mNCuruiM5GQA=CCCEF4B8"
PROJECT_KEY="MACHINECAP"
def connect_to_jira() -> JIRA:
    """
    Connects to a JIRA instance using credentials from environment variables.

    Returns:
        JIRA: An authenticated JIRA client instance.
    """
  
    if not all([JIRA_URL, EMAIL, API_TOKEN]):
        raise ValueError("JIRA credentials are not set in environment variables.")
    return JIRA(server=JIRA_URL, basic_auth=(EMAIL, API_TOKEN))

# Initialize JIRA client once
jira_client = connect_to_jira()

def create_jira_ticket(
    summary: str,
    description: str,
    issuetype: str,
    assignee: str,
    priority: str
) -> Dict[str, str]:
    """
    Creates a JIRA issue in the configured project using the provided details.

    Args:
        summary (str): The summary/title of the JIRA issue.
        description (str): The detailed description of the issue.
        issuetype (str): The type of the JIRA issue (e.g., 'Task', 'Bug').
        assignee (str): The assignee's username or email.
        priority (str): The priority of the issue (e.g., 'High', 'Medium', 'Low').

    Returns:
        dict: Information about the created JIRA issue, for example:
            {"issue_key": "MACHINECAP-123", "url": "https://your-jira-url/browse/MACHINECAP-123"}
        Or a dict indicating an error, for example:
            {"status": "error", "message": "Error details here"}
    """
    try:
        issue_dict = {
            'project': {'key': PROJECT_KEY},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issuetype},
            'priority': {'name': priority}
        }

        # Create the issue first
        new_issue = jira_client.create_issue(fields=issue_dict)

        # Assign the issue (Jira Cloud may require accountId instead of username/email)
        try:
            jira_client.assign_issue(new_issue.key, assignee)
        except Exception as assign_err:
            # Optionally, you can update the issue with the assignee field if direct assignment fails
            print(f"Warning: Could not assign issue directly: {assign_err}")

        print(f"Issue created: {new_issue.key}")
        return {
            "issue_key": new_issue.key,
            "url": f"{os.getenv('JIRA_URL')}/browse/{new_issue.key}"
        }
    except Exception as e:
        print(f"Error creating JIRA issue: {e}")
        return {
            "status": "error",
            "message": str(e)
        }
        
notification_agent = Agent(
    name="notification_agent",
    model="gemini-2.0-flash",
    description="Provides step-by-step assistance and diagnostic guidance to technicians for resolving machine issues based on predicted maintenance needs and detected anomalies.",
    instruction=NOTIFICATION_AGENT_INSTRUCTION,   
    tools=[*toolbox_tools, create_jira_ticket, publishDeviceNotification, createIncidentBridge, AgentTool(agent=rag_agent),] 
)