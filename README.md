![Alt text](https://https://github.com/capgcat/capgineered-meta-xr-ai-agents-/blob/main/images/00.png)

# Industrial AI Safety Suite: Intelligent Guidance for Safer Operations
Welcome to the Industrial AI Safety Suite—a next-generation, agentic platform designed to transform industrial safety and operational reliability. Our system leverages IoT monitoring, immersive XR/VR guidance, and centralized knowledge (RAG/Vector Store) to empower both technicians and SOC analysts, making industrial environments safer, smarter, and more efficient.

# 🌍 Explore the Project : Click below to navigate
🔍 [The Challenge: Risk & Inefficiency in Industrial Operations](#The Challenge: Risk & Inefficiency in Industrial Operations)  
💡 [Solution : Smart Concierge, FourSight Dashboard, Wayfinder](#our-solution)  
🤖 [Our Solution: The Agentic Safety Platform](#Our Solution: The Agentic Safety Platform)  
📱 [Meet the AI Agents](#Meet the AI Agents)  
🌐 [Solution Architecture](#solution-architecture)  
🧭 [Data Ingestion & Flow](#Data Ingestion & Flow) 
🌐 ADK Web & Mixed Reality Integration(#ADK Web & Mixed Reality Integration) 
🛠️ [Under the Hood: Our Technology Stack](#under-the-hood-our-technology-stack)  
💻 [Project Structure]](#project-setup-guide)
⚙️ [Technology Stack (#Technology Stack) 
🔐 [Quickstart: Project Setup Guide](#Quickstart: Project Setup Guide)  
🎬 [Live Demo Walkthrough](#live-demo-walkthrough)  
🚀 [What’s Next: Our Vision](#whats-next-our-vision-for-the-future)  
👨‍💻 [Contributors](#contributors)







# Existing Problem Overview
- Despite significant investments in safety manuals, operational guidelines, and audits, critical information remains fragmented and inconsistently applied. This leads to:
- Inefficient monitoring and delayed anomaly detection
- Prolonged incident resolution
- Increased risk and unplanned downtime


# Our Solution: The Agentic Safety Platform
We introduce a groundbreaking agentic system that centralizes all operational knowledge and delivers three core capabilities:
1. Intelligent Insights
Unified, up-to-date operational data via DataSage (Data Ingestion Agent)
Richer context for anomaly detection and prediction with Anomalyze (Anomaly Detection Agent)
Actionable problem descriptions for SOC and field technicians
2. Proactive Prevention (Self-Healing)
Predicts machine issues using IoT data with Predicta (Prediction Agent)
Automated adjustments (e.g., temperature/humidity) to prevent escalation via AutoTune (Self-Healing Agent)
3. Real-Time Immersive Guidance
Step-by-step XR/VR troubleshooting for technicians with GuideXR (Guidance Agent)
Proactive, intelligent insights for SOC analysts via InsightOps (SOC Notification Agent)
Automated SME coordination and guided incident resolution

# Meet the AI Agents
Agent Name	Role & Functionality
DataSage	Ingests and centralizes all operational and sensor data
Anomalyze	Detects anomalies and provides contextual alerts
Predicta	Predicts failures and recommends/prevents escalation
AutoTune	Executes self-healing actions (e.g., auto-adjusts machine parameters)
GuideXR	Delivers immersive, step-by-step XR/VR guidance to technicians
InsightOps	Notifies SOC analysts and orchestrates incident management

# Solution Architecture 
![Alt text](https://https://github.com/capgcat/capgineered-meta-xr-ai-agents-/blob/main/images/Architecture.png)

IoT Sensors → DataSage → RAG/Vector Store → Anomalyze/Predicta/AutoTune
GuideXR & InsightOps interface with users via XR/VR and web dashboards
Incident Management is orchestrated with automated SME coordination

# Data Ingestion & Flow
![Alt text](https://https://github.com/capgcat/capgineered-meta-xr-ai-agents-/blob/main/images/DataFlow.png)

IoT Sensors → DataSage → RAG/Vector Store → Anomalyze/Predicta/AutoTune
GuideXR & InsightOps interface with users via XR/VR and web dashboards
Incident Management is orchestrated with automated SME coordination
# Data Ingestion & Flow
![Alt text](https://https://github.com/capgcat/capgineered-meta-xr-ai-agents-/blob/main/images/flow.png)

Web Dashboard for SOC and management
Mixed Reality (XR/VR) for immersive technician guidance

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

# Technology Stack
Python 3.10+ (Poetry for dependency management)
Google Cloud Vertex AI (for agent deployment)
BigQuery (for sensor data storage)
XR/VR (Meta Quest, HoloLens, or compatible devices)
Web Dashboard (React/Next.js or similar)
RAG/Vector Store (for centralized knowledge)

# 🚀 Quickstart: Project Setup Guide
Install Poetry:
pip3 install poetry
Clone & Install:
cd meta-xr-ai-agents && poetry install
Activate Environment:
poetry env use python3 && source $(poetry env info --path)/bin/activate
Configure GCP:
gcloud auth application-default login
gcloud init
gcloud services enable aiplatform.googleapis.com
Run Locally:
adk web or adk run machine_sensors_ai_agents
Remote Deployment:
See Remote Deployment Instructions below.
# 🛡️ Safety and Security
Role-based access control for dashboards and agent actions
Data encryption in transit and at rest
Audit logs for all automated actions and recommendations
📊 BigQuery Schema
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
# 🎬 Live Demo Walkthrough
See It In Action:
Watch as our system detects an anomaly, suggests a self-healing action, and provides real-time XR guidance to a technician, while SOC analysts receive proactive notifications and incident coordination.
🔮 What’s Next: Our Vision
Deeper integration with legacy industrial systems
Expanded XR/VR capabilities for remote collaboration
Continuous learning from incident data to improve agent intelligence
👨‍💻 Contributors

# Installation steps
1. pip3 install poetry
2. cd meta-xr-ai-agents
3. poetry install
4. poetry env use python3
5. source $(poetry env info --path)/bin/activate
6. gcloud auth application-default login (update values in .env)
7. gcloud init (Select project-id)
8. gcloud services enable aiplatform.googleapis.com
9. adk web or adk run machine_sensors_ai_agents

## Remote deployment to Vertex AI Engine
10. poetry run deploy-remote --create
11. poetry run deploy-remote --create_session --resource_id=your-resource-id
               or
    POST https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/reasoningEngines/AGENT_ENGINE_ID/sessions
    Authorization Bearer : Create it by running "gcloud auth print-access-token"
13. poetry run deploy-remote --send --resource_id=your-resource-id --session_id=your-session-id --message="The cat was a funny cat. The cat liked to sleep, and the cat liked to eat. Every morning, the cat would jump on the bed, the cat would meow, and the cat would purr. Everyone in the house knew the cat, talked about the cat, and cared for the cat. It was always the cat, the cat, the cat — nothing but the cat all day long."
14. poetry run deploy-remote --delete --resource_id=your-resource-id

# MCP Toolbox setup
1. curl -O https://storage.googleapis.com/genai-toolbox/v0.7.0/darwin/arm64/toolbox
   Note : Replace your os above. one of linux/amd64, darwin/arm64, darwin/amd64, or windows/amd64
2. chmod +x toolbox
3. ./toolbox --tools-file "/Users/sandeepkudterkar/Google Cloud Agents/hackathon/meta-xr-ai-agents/deployment/mcp-toolbox/tools.yaml"
   Note : Modify the above path.


# Schema for BQ
```text
[
  {"name": "timestamp", "type": "TIMESTAMP", "mode": "REQUIRED", "description": "Timestamp when the observation was recorded (UTC)."},
  {"name": "machine_id", "type": "STRING", "mode": "REQUIRED", "description": "Unique identifier for the machine."},
  {"name": "observation_type", "type": "STRING", "mode": "REQUIRED", "description": "Categorization of the observation (e.g., 'temperature_reading', 'pressure_reading', 'vibration_magnitude', 'current_draw', 'flow_rate', 'rpm', 'gauge_reading', 'indicator_light_status', 'component_visual_state')."},
  {"name": "sensor_id", "type": "STRING", "mode": "REQUIRED", "description": "Specific identifier for the individual sensor or component."},
  {"name": "numeric_value", "type": "FLOAT", "mode": "NULLABLE", "description": "The numeric value of the observation."},
  {"name": "unit", "type": "STRING", "mode": "NULLABLE", "description": "Unit of the numeric_value (e.g., 'Celsius', 'PSI', 'Amps', 'RPM')."},
  {"name": "string_value", "type": "STRING", "mode": "NULLABLE", "description": "A string value for categorical observations."},
  {"name": "image_url", "type": "STRING", "mode": "NULLABLE", "description": "Google Cloud Storage URL to the source image if data originated from a visual inspection agent."},
  {"name": "bounding_box_coordinates", "type": "STRING", "mode": "NULLABLE", "description": "JSON string for bounding box coordinates [x, y, width, height]."},
  {"name": "observation_confidence", "type": "FLOAT", "mode": "NULLABLE", "description": "Confidence score for the visual observation."},
  {"name": "threshold_lower", "type": "FLOAT", "mode": "NULLABLE", "description": "Mention Lower Threshold"},
  {"name": "threshold_upper", "type": "FLOAT", "mode": "NULLABLE", "description": "Mention Lower Threshold"},
  {"name": "ideal_visual_state", "type": "STRING", "mode": "NULLABLE", "description": "Ideal Visual State"}
 ]
```
