
from google.adk import Agent
from google.adk.agents import SequentialAgent

from machine_sensors_ai_agents.sub_agents.image_desc_generation.agent import image_desc_generation_agent
from machine_sensors_ai_agents.sub_agents.data_import.agent import data_import_agent
from machine_sensors_ai_agents.sub_agents.decode_message.agent import decode_message_agent



data_ingestion_agent = SequentialAgent(
    name="data_ingestion_agent",
    description=(
        'Data ingestion agent for IoT machine sensors. '
        'This agent is responsible for image description generation and data import tasks. '
        'It calls the image description generation agent to generate descriptions for images '
        'captured by sensors, and the data import agent to handle the import of sensor data. '
        'And finally, saving the output of these tasks to BigQuery for further analysis and processing.'
    ),
    sub_agents=[image_desc_generation_agent, data_import_agent],

)