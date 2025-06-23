from google.adk.agents import Agent
from .prompt import GUIDANCE_AGENT_INSTRUCTION
from google.adk.tools.tool_context import ToolContext
from typing import Optional, List, Dict
from .tools import toolbox_tools
from machine_sensors_ai_agents.sub_agents.rag_agent_guidance.agent import rag_agent_guidance

from jira import JIRA
from dotenv import load_dotenv
import os

# Load environment variables
JIRA_URL="https://capgineered-agents-machine.atlassian.net/"
EMAIL=""
API_TOKEN= ""
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

def fetch_jira_ticket(   
    issue_key: Optional[str] = None,
    summary: Optional[str] = None,
    description: Optional[str] = None,
    issuetype: Optional[str] = None,
    project_key: Optional[str] = None
) -> Dict[str, str]:
    """
    Fetches a JIRA issue by issue key or by searching with summary/description/issuetype.

    Args:       
        issue_key (str, optional): The JIRA issue key (e.g., 'MACHINECAP-123').
        summary (str, optional): The summary/title of the JIRA issue.
        description (str, optional): The detailed description of the issue.
        issuetype (str, optional): The type of the JIRA issue (e.g., 'Task', 'Bug').
        project_key (str, optional): The JIRA project key (e.g., 'MACHINECAP').

    Returns:
        dict: Information about the fetched JIRA issue, for example:
            {
                "issue_key": "MACHINECAP-123",
                "url": "https://your-jira-url/browse/MACHINECAP-123",
                "summary": "...",
                "description": "...",
                "status": "...",
                "assignee": "...",
                "priority": "..."
            }
        Or a dict indicating an error, for example:
            {"status": "error", "message": "Error details here"}
    """
    try:
        if issue_key:
            # Fetch by issue key
            issue = jira_client.issue(issue_key)
            return {
                "issue_key": issue.key,
                "url": f"{os.getenv('JIRA_URL')}/browse/{issue.key}",
                "summary": issue.fields.summary,
                "description": issue.fields.description,
                "status": issue.fields.status.name,
                "assignee": getattr(issue.fields.assignee, 'emailAddress', None) if issue.fields.assignee else None,
                "priority": issue.fields.priority.name if issue.fields.priority else None
            }
        else:
            # Build JQL query for search
            jql = []
            if project_key:
                jql.append(f'project="{project_key}"')
            if summary:
                jql.append(f'summary~"{summary}"')
            if description:
                jql.append(f'description~"{description}"')
            if issuetype:
                jql.append(f'issuetype="{issuetype}"')
            if not jql:
                return {"status": "error", "message": "No search parameters provided."}
            jql_query = " AND ".join(jql)
            issues = jira_client.search_issues(jql_query, maxResults=1)
            if not issues:
                return {"status": "error", "message": "No matching Jira ticket found."}
            issue = issues[0]
            return {
                "issue_key": issue.key,
                "url": f"{os.getenv('JIRA_URL')}/browse/{issue.key}",
                "summary": issue.fields.summary,
                "description": issue.fields.description,
                "status": issue.fields.status.name,
                "assignee": getattr(issue.fields.assignee, 'emailAddress', None) if issue.fields.assignee else None,
                "priority": issue.fields.priority.name if issue.fields.priority else None
            }
    except Exception as e:
        print(f"Error fetching JIRA issue: {e}")
        return {
            "status": "error",
            "message": str(e)
        }
        
guidance_agent = Agent(
    name="guidance_agent",
    model="gemini-2.5-pro",
    description="Provides step-by-step assistance and diagnostic guidance to technicians for resolving machine issues based on predicted maintenance needs and detected anomalies.",
    instruction=GUIDANCE_AGENT_INSTRUCTION,
    sub_agents=[rag_agent_guidance],  # Include the rag_agent_guidance for RAG capabilities
    tools=[*toolbox_tools, fetch_jira_ticket]
)