![Alt text](https://github.com/user-attachments/assets/3c785ed9-c064-4b39-8c1d-534b0d388c22)

# Industrial AI Safety Suite: Intelligent Guidance for Safer Operations
Welcome to the Industrial AI Safety Suite—a next-generation, agentic platform designed to transform industrial safety and operational reliability. Our system leverages IoT monitoring, immersive XR/VR guidance, and centralized knowledge (RAG/Vector Store) to empower both technicians and SOC analysts, making industrial environments safer, smarter, and more efficient.

# 🌍 Explore the Project : Click below to navigate
🔍 [Problem Statement and Target Users](#the-challenge-risk--inefficiency-in-industrial-operations)  
🤖 [Solution and Technical Components](#our-solution-the-agentic-safety-platform)
🚀 [Meet the AI Agents](#meet-the-ai-agents)  
📱 [Relevant Metrics](#relevant-metrics)
🌐 [Execution Plan](#execution-agents)   
🧭 [Data Ingestion & Flow](#data-ingestion--flow)
🛠️ [Under the Hood: Our Technology Stack](#technology-stack)  
💻 [Project Structure](#exploring-the-codebase)  
🔐 [Quickstart: Project Setup Guide](#quickstart-project-setup-guide)  
🎬 [Live Demo Walkthrough](#live-demo-walkthrough)  
🚀 [What’s Next: Our Vision](#whats-next-our-vision)  
👨‍💻 [Contributors](#contributors)


# Problem Statement and Target Users
## Problem Statement:
Industrial operations depend on complex, high-value machinery where unplanned downtime, slow repairs, or incorrect maintenance can cause significant financial losses, safety risks, and productivity drops. Traditional maintenance is often reactive, siloed, and lacks real-time intelligence, leading to delayed fault detection, inefficient troubleshooting, and increased risk of human error—especially for less experienced technicians.
- Despite significant investments in safety manuals, operational guidelines, and audits, critical information remains fragmented and inconsistently applied. This leads to:
- Inefficient monitoring and delayed anomaly detection
- Prolonged incident resolution
- Increased risk and unplanned downtime

## Target Users:

- **Maintenance Technicians:** Need real-time, step-by-step guidance to perform complex repairs safely and efficiently.
- **Operations Managers:** Require predictive insights to minimize downtime and optimize maintenance schedules.
- **Industrial Safety Officers:** Need assurance that maintenance follows safety protocols and compliance standards.
- **IT/OT Administrators:** Responsible for integrating secure, scalable AI solutions with existing IoT and enterprise systems.




# Solution and Technical Components
## Overview:
The solution is a GenAI-powered, agentic mixed reality maintenance system that integrates IoT sensor data, cloud-based AI, and Meta Quest 3 AR headsets. It delivers real-time anomaly detection, predictive maintenance, prioritized notifications, and immersive AR-guided repair procedures.
## Solution Architecture
![image](https://github.com/user-attachments/assets/520a1913-0af9-4f82-b4ff-332b090beb59)

## Key Features:

- **Real-time Anomaly Detection:** AI agents continuously analyze sensor data (temperature, vibration, current, etc.) to detect abnormal patterns.
- **Predictive Maintenance:** ML models forecast potential failures, enabling proactive interventions.
- **Automated Notifications & Escalation:** Alerts are prioritized and sent via email, SMS, or push notifications based on severity and urgency.
- **AR Guidance:** Meta Quest 3 overlays step-by-step repair instructions and virtual manuals directly onto the affected machinery, reducing error rates and training time.
- **Secure Data Flow:** Ensures compliance with safety protocols and secure transmission from IoT sensors to cloud and headset.


## Technical Components:
- **Google Agentic AI Tools:**
- **Gemini 2.0 Flash:** For fast, accurate LLM-based reasoning and guidance.
- **Vertex AI:** For ML model deployment and real-time inference (if used).

## APIs & Integrations:- 
- **IoT Sensor APIs:** For real-time data ingestion.
- **Jira API:** For automated ticket creation and dashboard integration.
- **Meta Quest 3 SDK:** For AR overlay and headset integration.
## Datasets:
- Historical and real-time sensor data.
- Maintenance logs and manuals.
- Anomaly and failure event datasets.
## 3rd Party Tools:
- Jira (for ticketing and dashboards).
- Cloud storage (for manuals, images, logs).

# Meet the AI Agents
Our AI-driven platform orchestrates a suite of specialized agents to deliver end-to-end, proactive machine monitoring, maintenance, and incident response. The core orchestrator, **Machine Sensor AI Agent**, coordinates two main flows: monitoring and technician guidance.

**Core & Orchestration Agents:**
- **Machine Sensor AI Agent (machine_sensor_ai_agent) (Root Agent)**
The primary orchestrator for IoT machine sensors. This agent manages sensor data collection, analysis, and control operations, providing guidance to technicians. It delegates tasks to specialized sub-agents such as the monitoring_agent for data processing and the guidance_agent for support.

- **Monitoring Agent (monitoring_agent)**
Responsible for the overall health and performance monitoring of machine sensors. It sequentially manages data ingestion, then passes the data to detection agents for anomaly identification and predictive maintenance.

- **Detection Agent (detection_agent)**
Focuses on identifying issues within sensor data. It runs anomaly detection and predictive maintenance tasks in parallel to find current problems and forecast potential future failures. Its sub-agents (anomaly and prediction agents) typically invoke the notification_agent.

- **Guidance Agent:**
GuideXR delivers immersive, step-by-step XR/VR guidance to technicians, accelerating repairs and reducing errors.Provides step-by-step, actionable assistance and diagnostic guidance to technicians. It helps resolve machine issues based on predicted maintenance needs, detected anomalies, and information retrieved via a specialized RAG Agent for Guidance. This agent will also be used for SOC specialists and incident bridge calls.

**Specialized Sub-Agents:**
- **Anomaly Detection Agent (anomaly_agent)**
Identifies abnormal patterns, unusual operational behavior, or deviations from normal sensor readings in real-time industrial sensor data. It utilizes a RAG agent for contextual information and can trigger notifications.

- **Data Import Agent (data_import_agent)**
Processes incoming data, primarily from the image_description_generation_agent. It ensures data is correctly structured, uses a RAG agent to determine sensor status based on operational context, and prepares the data for insertion into BigQuery.

- **Data Ingestion Agent (data_ingestion_agent)**
Manages the initial stages of data intake. It orchestrates the generation of image descriptions (if applicable) and then the data import process, ultimately ensuring sensor data is saved for further analysis.

- **Image Description Generation Agent (image_desc_generation_agent)**
An expert image analysis assistant. Its primary task is to describe images provided via Google Cloud Storage (GCS) URIs, using tools to fetch and analyze these images.

- **Notification Agent (notification_agent)**
Monitors machine anomalies and is responsible for creating Jira tickets for detected issues. It ensures tickets are correctly assigned and escalated based on predefined business rules and the severity of the anomaly, and can use a RAG agent for context.

- **Prediction Maintenance Agent (prediction_maintainence_agent)**
Analyzes anomaly alerts and historical data to forecast potential equipment failures. It recommends proactive maintenance actions, utilizing a RAG agent for broader contextual information and historical data, and can trigger notifications.

- **RAG Agent (rag_agent)**
An AI assistant that provides accurate and concise answers to questions by retrieving information from a specialized Retrieval Augmented Generation (RAG) corpus of documents. It is used by various other agents to fetch operational norms, historical data, and other relevant information.

- **RAG Agent for Guidance (rag_agent_guidance)**
Similar to the general RAG Agent, but this one is specifically configured to retrieve information from a RAG corpus dedicated to maintenance guidance, repair instructions, schematics, and technical documentation to support the guidance_agent. 

![image](https://github.com/user-attachments/assets/520a1913-0af9-4f82-b4ff-332b090beb59)

# Data Ingestion & Flow
![Alt text](https://github.com/user-attachments/assets/7decd02c-287c-4da0-9d7c-aaf2cfeba928)
![Alt text](https://github.com/user-attachments/assets/84053662-4f1a-4925-aec5-2fdd797618cb)
- Continuous ingestion of sensor, visual, and manual data
- Centralized knowledge base for up-to-date context
- Real-time feedback loop for anomaly detection, prediction, and guidance

# Under the Hood: Our Technology Stack
- **Python 3.10+** (Poetry for dependency management)
- **Google Cloud Vertex AI**(for agent deployment) 
- **BigQuery** (for sensor data storage)
- **XR/VR** (Meta Quest, HoloLens, or compatible devices)
- **Web Dashboard**(React/Next.js or similar) 
- **RAG/Vector Store**(for centralized knowledge)

# Project Structure
```text
## Project Structure
.
├── README.md
├── deployment
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   └── remote.cpython-313.pyc
│   ├── cleanup.py
│   └── remote.py
├── eval
│   ├── __init__.py
│   └── eval.py
├── machine_sensors_ai_agents
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   └── agent.cpython-313.pyc
│   ├── agent.py
│   ├── prompt.py
│   └── sub_agents
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-313.pyc
│       ├── anomaly_detection
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── prompt.py
│       │   └── tools.py
│       ├── basic_demo_agent
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   │   ├── __init__.cpython-313.pyc
│       │   │   ├── agent.cpython-313.pyc
│       │   │   ├── prompt.cpython-313.pyc
│       │   │   └── tools.cpython-313.pyc
│       │   ├── agent.py
│       │   ├── prompt.py
│       │   └── tools.py
│       ├── data_ingestion
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── prompt.py
│       │   └── tools.py
│       ├── guidance
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── prompt.py
│       │   └── tools.py
│       ├── notification
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── prompt.py
│       │   └── tools.py
│       └── prediction
│           ├── __init__.py
│           ├── agent.py
│           ├── prompt.py
│           └── tools.py
├── poetry.lock
├── pyproject.toml
├── tests
│   └── test_agents.py
└── ui
    ├── mixed-reality
    │   └── mixed-reality.json
    └── web
        └── web.json
```

# Quickstart: Project Setup Guide
- **Install Poetry:**
pip3 install poetry
- **Clone & Install:**
cd meta-xr-ai-agents && poetry install
- **Activate Environment:**
poetry env use python3 && source $(poetry env info --path)/bin/activate
- **Configure GCP:** 
gcloud auth application-default login
- **gcloud init**
gcloud services enable aiplatform.googleapis.com
- **Run Locally:**
adk web or adk run machine_sensors_ai_agents
- **Remote Deployment:**
1 poetry run deploy-remote --create
2 poetry run deploy-remote --create_session --resource_id=your-resource-id
               or
    POST https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/reasoningEngines/AGENT_ENGINE_ID/sessions
    Authorization Bearer : Create it by running "gcloud auth print-access-token"
3 poetry run deploy-remote --send --resource_id=your-resource-id --session_id=your-session-id --message="The cat was a funny cat. The cat liked to sleep, and the cat liked to eat. Every morning, the cat would jump on the bed, the cat would meow, and the cat would purr. Everyone in the house knew the cat, talked about the cat, and cared for the cat. It was always the cat, the cat, the cat — nothing but the cat all day long."
4 poetry run deploy-remote --delete --resource_id=your-resource-id

# Safety and Security
- Role-based access control for dashboards and agent actions
- Data encryption in transit and at rest
- Audit logs for all automated actions and recommendations
- **BigQuery Schema:**
[
  {"name": "timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"},
  {"name": "machine_id", "type": "STRING", "mode": "REQUIRED"},
  {"name": "observation_type", "type": "STRING", "mode": "REQUIRED"},
  {"name": "sensor_id", "type": "STRING", "mode": "REQUIRED"},
  {"name": "numeric_value", "type": "FLOAT", "mode": "NULLABLE"},
  {"name": "unit", "type": "STRING", "mode": "NULLABLE"},
  {"name": "string_value", "type": "STRING", "mode": "NULLABLE"},
  {"name": "image_url", "type": "STRING", "mode": "NULLABLE"},
  {"name": "bounding_box_coordinates", "type": "STRING", "mode": "NULLABLE"},
  {"name": "observation_confidence", "type": "FLOAT", "mode": "NULLABLE"},
  {"name": "threshold_lower", "type": "FLOAT", "mode": "NULLABLE"},
  {"name": "threshold_upper", "type": "FLOAT", "mode": "NULLABLE"},
  {"name": "ideal_visual_state", "type": "STRING", "mode": "NULLABLE"}
]
# Live Demo Walkthrough
See It In Action:

Watch as our system detects an anomaly, suggests a self-healing action, and provides real-time XR guidance to a technician, while SOC analysts receive proactive notifications and incident coordination.

# What’s Next: Our Vision
Deeper integration with legacy industrial systems
Expanded XR/VR capabilities for remote collaboration
Continuous learning from incident data to improve agent intelligence

# Contributors
