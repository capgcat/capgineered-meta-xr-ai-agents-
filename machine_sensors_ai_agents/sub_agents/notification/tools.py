from datetime import datetime
import os

from toolbox_core import ToolboxSyncClient

from dotenv import load_dotenv
from google.adk.tools import FunctionTool, ToolContext



# Load environment variables
load_dotenv()

# ----- Example of Google Cloud Tools (MCP Toolbox for Databases) -----
TOOLBOX_URL = os.getenv("MCP_TOOLBOX_URL", "http://127.0.0.1:5000")

# Initialize Toolbox client
toolbox = ToolboxSyncClient(TOOLBOX_URL)
# Load all the tools from toolset
toolbox_tools = toolbox.load_toolset("notifications-toolset")
    
def publishDeviceNotification(machine_id: str, sensor_adjustment_type: str, values: str):
    """
    Publishes a device push notification to pubsub to adjust sensor values.
    """
    
    if not machine_id or not sensor_adjustment_type or not values:
        print("Invalid parameters provided for device notification.")
        return {"status": "error", "message": "Invalid parameters"}

    # Construct the message payload
    message = {
        "machine_id": machine_id,
        "sensor_adjustment_type": sensor_adjustment_type,
        "values": values,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Publish to Pub/Sub (assuming a topic is configured)
    try:
        topic_name = f"projects/{os.getenv('GOOGLE_CLOUD_PROJECT')}/topics/device-notifications"
        from google.cloud import pubsub_v1
        publisher = pubsub_v1.PublisherClient()
        future = publisher.publish(topic_name, str(message).encode('utf-8'))
        future.result()  # Wait for the publish to complete
        print(f"Notification published for {machine_id}")
        return {"status": "success", "message": "Notification published"}
    except Exception as e:
        print(f"Error publishing notification: {e}")
        return {"status": "error", "message": str(e)}
    

def createIncidentBridge(jira_ticket_id: str, title: str, description: str, priority: str, assignee_emails: list):
    """
    Creates an incident bridge in the Incident Management system.

    Args:
        jira_ticket_id (str): The ID of the JIRA ticket associated with the incident.
        title (str): The title of the incident.
        description (str): A detailed description of the incident.
        priority (str): The priority level of the incident (e.g., 'High', 'Medium', 'Low').
        assignee_emails (list): List of email addresses to assign to the incident.

    Returns:
        dict: Information about the created incident bridge, for example:
            {"incident_id": "INC-12345", "url": "https://your-incident-management-url/INC-12345"}
        Or a dict indicating an error, for example:
            {"status": "error", "message": "Error details here"}
    """
    # Placeholder for actual implementation
    return {
        "incident_id": "INC-{jira_ticket_id}",
        "title": title,
        "url": f"{os.getenv('INCIDENT_MANAGEMENT_URL')}/INC-{jira_ticket_id}",
    }

    
publishDeviceNotification = FunctionTool(publishDeviceNotification)
createIncidentBridge = FunctionTool(createIncidentBridge)
