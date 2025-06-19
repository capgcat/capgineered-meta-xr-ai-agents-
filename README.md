![Alt text](https://github.com/user-attachments/assets/3c785ed9-c064-4b39-8c1d-534b0d388c22)

# Industrial AI Safety Suite: Intelligent Guidance for Safer Operations
Welcome to the Industrial AI Safety Suite—a next-generation, agentic platform designed to transform industrial safety and operational reliability. Our system leverages IoT monitoring, immersive XR/VR guidance, and centralized knowledge (RAG/Vector Store) to empower both technicians and SOC analysts, making industrial environments safer, smarter, and more efficient.

# 🌍 Explore the Project : Click below to navigate
🔍 [The Challenge: Risk & Inefficiency in Industrial Operations](#the-challenge-risk--inefficiency-in-industrial-operations)  
🤖 [Solution: Insights, Self-Healing, Real-Time Immersive Guidance](#our-solution-the-agentic-safety-platform)  
📱 [Meet the AI Agents](#meet-the-ai-agents)  
🌐 [Solution Architecture](#solution-architecture)  
🧭 [Data Ingestion & Flow](#data-ingestion--flow)  
🌐 [ADK Web & Mixed Reality Integration](#adk-web--mixed-reality-integration)  
🛠️ [Under the Hood: Our Technology Stack](#technology-stack)  
💻 [Project Structure](#exploring-the-codebase)  
🔐 [Quickstart: Project Setup Guide](#quickstart-project-setup-guide)  
🎬 [Live Demo Walkthrough](#live-demo-walkthrough)  
🚀 [What’s Next: Our Vision](#whats-next-our-vision)  
👨‍💻 [Contributors](#contributors)


# The Challenge: Risk & Inefficiency in Industrial Operations
- Despite significant investments in safety manuals, operational guidelines, and audits, critical information remains fragmented and inconsistently applied. This leads to:
- Inefficient monitoring and delayed anomaly detection
- Prolonged incident resolution
- Increased risk and unplanned downtime


# Our Solution: The Agentic Safety Platform
We introduce a groundbreaking agentic system that centralizes all operational knowledge and delivers three core capabilities:
- **1. Intelligent Insights**
Unified, up-to-date operational data via DataSage (Data Ingestion Agent)
Richer context for anomaly detection and prediction with Anomalyze (Anomaly Detection Agent)
Actionable problem descriptions for SOC and field technicians
- **2. Proactive Prevention (Self-Healing)** 
Predicts machine issues using IoT data with Predicta (Prediction Agent)
Automated adjustments (e.g., temperature/humidity) to prevent escalation via AutoTune (Self-Healing Agent)
- **3. Real-Time Immersive Guidance** 
Step-by-step XR/VR troubleshooting for technicians with GuideXR (Guidance Agent)
Proactive, intelligent insights for SOC analysts via InsightOps (SOC Notification Agent)
Automated SME coordination and guided incident resolution

# Meet the AI Agents
Our AI-driven platform orchestrates a suite of specialized agents to deliver end-to-end, proactive machine monitoring, maintenance, and incident response. The core orchestrator, **Machine Sensor AI Agent**, coordinates two main flows: monitoring and technician guidance.
- **Monitoring Agent (with subagents):**

**DataSage** ingests and centralizes all operational and sensor data, creating a unified data foundation.
**Anomalyze** continuously detects anomalies, providing contextual alerts for early issue identification.
**Predicta** leverages historical and real-time data to predict failures and recommend preventive actions, reducing unplanned downtime.
**AutoTune** executes self-healing actions, such as auto-adjusting machine parameters, to resolve issues autonomously and minimize manual intervention.
**InsightOps** notifies SOC analysts and orchestrates incident management, ensuring rapid response and compliance.
- ** Guidance Agent:**
GuideXR delivers immersive, step-by-step XR/VR guidance to technicians, accelerating repairs and reducing errors.

# Solution Architecture
![Alt text](https://github.com/user-attachments/assets/72ac236c-8f63-4e8d-8495-51fc95e45ba2)
- **IoT Sensors → DataSage → RAG/Vector Store → Anomalyze/Predicta/AutoTune** 
- GuideXR & InsightOps interface with users via XR/VR and web dashboards
- Incident Management is orchestrated with automated SME coordination

# Data Ingestion & Flow
![Alt text](https://github.com/user-attachments/assets/7decd02c-287c-4da0-9d7c-aaf2cfeba928)
![Alt text](https://github.com/user-attachments/assets/84053662-4f1a-4925-aec5-2fdd797618cb)
- Continuous ingestion of sensor, visual, and manual data
- Centralized knowledge base for up-to-date context
- Real-time feedback loop for anomaly detection, prediction, and guidance

# ADK Web & Mixed Reality Integration
- **Web Dashboard** for SOC and management
- **Mixed Reality (XR/VR)**  for immersive technician guidance
![image](https://github.com/user-attachments/assets/f6ffce78-202e-4d21-b6a7-7eb4da2a12a6)


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
