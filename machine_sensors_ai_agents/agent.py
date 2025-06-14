from google.adk.agents import LlmAgent,SequentialAgent
from .sub_agents.basic_demo_agent import basic_demo_agent
from .sub_agents.guidance.agent import guidance_agent
from .sub_agents.anomaly_detection.agent import anomaly_agent
from .sub_agents.prediction.agent import prediction_maintainence_agent
from .sub_agents.data_ingestion.agent import data_ingestion_agent

machine_sensor_ai_agent = SequentialAgent(
    #model="gemini-2.0-flash",
    name='machine_sensor_ai_agent',
    description=(
       'IoT agents for monitoring and controlling machine sensors. '
        'This agent can handle tasks related to machine sensor data collection, '
        'analysis, and control operations. It is designed to work with various types of sensors '
        'and can be integrated into larger IoT systems for real-time monitoring and automation.'
    ),
    sub_agents=[data_ingestion_agent, anomaly_agent, prediction_maintainence_agent],
)

root_agent = machine_sensor_ai_agent
