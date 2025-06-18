from google.adk.agents import LlmAgent,SequentialAgent
from .sub_agents.basic_demo_agent import basic_demo_agent
from .sub_agents.guidance.agent import guidance_agent
from .sub_agents.anomaly_detection.agent import anomaly_agent
from .sub_agents.prediction.agent import prediction_maintainence_agent
from .sub_agents.data_ingestion.agent import data_ingestion_agent
from .sub_agents.notification.agent import notification_agent
from .sub_agents.rag_agent.agent import rag_agent


monitoring_agent = SequentialAgent(
    #model="gemini-2.0-flash",
    name='monitoring_agent',
    description=(
        'You are a monitoring agent for IoT machine sensors. '
        'Your primary role is to monitor the health and performance of machine sensors, '
        'detect anomalies, and predict maintenance needs. '
    ),
    sub_agents=[data_ingestion_agent, anomaly_agent, prediction_maintainence_agent,notification_agent],
)

machine_sensor_ai_agent = LlmAgent(
    model="gemini-2.0-flash",
    name='machine_sensor_ai_agent',
    description=(
        "IoT agents for monitoring and controlling machine sensors. "
        "This agent can handle tasks related to machine sensor data collection, "
        "analysis, and control operations. "
        "It can also provide guidance and support for technicians in diagnosing and resolving machine issues. "
        "If you are given a JSON object with sensor data, use the `monitoring_agent` to process it. "
        "If asked about guidance, you can refer to the `guidance_agent` for step-by-step assistance. "
    ),
    sub_agents=[monitoring_agent, guidance_agent],
)

root_agent = machine_sensor_ai_agent
