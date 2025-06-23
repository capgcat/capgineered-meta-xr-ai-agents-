![Alt text](https://github.com/user-attachments/assets/9be3f842-e963-49a2-a2bf-0dd7cb3a39cb)

# Industrial AI Safety Suite: Intelligent Guidance for Safer Operations
Welcome to the Industrial AI Safety Suite—a next-generation, agentic platform designed to transform industrial safety and operational reliability. Our system leverages IoT monitoring, immersive XR/VR guidance, and centralized knowledge (RAG/Vector Store) to empower both technicians and SOC analysts, making industrial environments safer, smarter, and more efficient.

# 🌍 Explore the Project : Click below to navigate
🔍 [Problem Statement and Target Users](#problem-statement-and-target-users)  
🤖 [Solution and Technical Components](#solution-and-technical-components)
🚀 [Meet the AI Agents](#meet-the-ai-agents)
📊 [Dashboard - Web & Jira](#dashboard---web--jira)  
👓 [Mixed Reality Guidance on Meta Headset ](#mixed-reality-guidance-on-meta-headset)   
📱 [Relevant Metrics](#relevant-metrics)  
🌐 [Execution Plan](#execution-plan)  
🧭 [Data Ingestion & Flow](#data-ingestion--flow)  
🛠️ [Under the Hood: Our Technology Stack with Modern MCP Tools Box](#under-the-hood-our-technology-stack)  
💻 [Project Structure](#project-structure)  
🔐 [Quickstart: Project Setup Guide](#quickstart-project-setup-guide)  
👓 [How to Run This Project on Meta Quest 3](#how-to-run-this-project-on-meta-quest-3)  
🎬 [Live Demo Walkthrough](#live-demo-walkthrough)  
🚀 [What’s Next: Our Vision](#whats-next-our-vision)  
👨‍💻 [Contributors](#contributors)


# Problem Statement and Target Users
## Problem Statement:
Industrial operations depend on complex, high-value machinery where unplanned downtime, slow repairs, or incorrect maintenance can cause significant financial losses, safety risks, and productivity drops. Traditional maintenance is often reactive, siloed, and lacks real-time intelligence, leading to delayed fault detection, inefficient troubleshooting, and increased risk of human error—especially for less experienced technicians.
Despite significant investments in safety manuals, operational guidelines, and audits, critical information remains fragmented and inconsistently applied. This leads to:
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
![image](https://github.com/user-attachments/assets/a7117881-a8da-49eb-bef1-407796303870)

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
![Alt text](https://github.com/user-attachments/assets/4f702489-a63d-41ae-821b-d6f2eb64d5c7)
- **Prediction Maintenance Agent (prediction_maintainence_agent)**
Analyzes anomaly alerts and historical data to forecast potential equipment failures. It recommends proactive maintenance actions, utilizing a RAG agent for broader contextual information and historical data, and can trigger notifications.

- **RAG Agent (rag_agent)**
An AI assistant that provides accurate and concise answers to questions by retrieving information from a specialized Retrieval Augmented Generation (RAG) corpus of documents. It is used by various other agents to fetch operational norms, historical data, and other relevant information.

- **RAG Agent for Guidance (rag_agent_guidance)**
Similar to the general RAG Agent, but this one is specifically configured to retrieve information from a RAG corpus dedicated to maintenance guidance, repair instructions, schematics, and technical documentation to support the guidance_agent. 

![image](https://github.com/user-attachments/assets/61d5eced-8943-44e5-879c-6ce9d865aca1)

# Dashboard - Web & Jira
**Deployment & Distribution:**
- **Jira Web Dashboard and Jira Integration:**********
- For managers to view real-time machine health, alerts, and 
- Automated ticket creation and status tracking for maintenance events.
- Comprehensive analytics and compliance tools to maximize uptime and ensure on-site safety.
![Alt text](https://github.com/user-attachments/assets/402cdd33-da66-4b31-b780-b48ecc00ae4c)
- **B5META Mixed Reality Maintenance Dashboard:** 
- This web-based application offers a comprehensive overview of pending tasks for the Maintenance Technicians, Operations Managers,IT/OT Administrators and Industrial Safety Officers. It highlights high-priority items to ensure a seamless process while keeping teams organized and focused on urgent tasks, thereby ensuring timely completion and accountability.
- The app provides insights into tasks by breaking it down using multiple views for dashboard.
It integrates AI agents to efficiently respond to user queries, such as retrieving the top pending tasks in specific areas. 
![Alt text](https://github.com/user-attachments/assets/423c5618-9f37-4ae7-81df-27bcd4a4ffed)


# Mixed Reality Guidance on Meta Headset 
![image](https://github.com/capgcat/capgineered-meta-xr-ai-agents-/blob/1dc64973711202b56133bceadd3b653af9bab884/images/MixedReality.jpg)
- All Mixed Reality panels and their functionalities are powered by integrated AI agents, driving intelligent data processing and real-time guidance.
- A cutting-edge Mixed Reality application designed to provide real-time engineer guidance for machine maintenance and repair.
- Leverages anomaly detection and predictive insights from our specialized anomaly and prediction AI agents to generate context-aware, actionable troubleshooting steps.
- Features a prominent central holographic panel ("Welcome to Cappgineered Guidance Agent") that:
- Includes a search bar for quick navigation,
- Delivers dynamic, step-by-step repair instructions (e.g., "Troubleshooting: Actuator," "Troubleshooting: Motor") provided by an intelligent guidance agent,
- Highlights "Essential Machine Modules" with distinct icons, allowing for quick access to component-specific information.
- Includes a left holographic panel ("Machine Configuration & Diagnostics & Sensor Controls") for system management:
- Machine Configuration: Allows selection/enabling of system types like Electrical, Hydraulic, Pneumatic, Calibration, High Frequency, Energy Management, and Audit.
- Diagnostics & Sensor Controls: Provides options for viewing Anomalies and Report Logs.
- Displays a right holographic panel ("Machine Parameter Set") showing critical, adjustable machine parameters with sliders and value displays for Vibration Amplitude (mm/s), Coolant Temperature (°C), Air Pressure (psi), Spindle Speed (RPM), Sensor Noise Level (dB), Voltage Fluctuation, Signal-to-Noise Ratio.
- Enables interactive adjustment of parameters using intuitive sliders displayed holographically in the engineer's field of view.
- Offers specific guidance for common machine components, such as actuators, motors, valves, gears, and bearings, directly tied to sensor warnings and diagnostic information.
- Integrates Thermal Control System data and supports a Predictive Maintenance Mode for proactive issue resolution, enhancing overall machine uptime.

# Relevant Metrics
## AI System Performance:
![image](https://github.com/user-attachments/assets/d0d38901-b5ee-4c0e-8bfb-febb25f9ec52)
### Anomaly Detection(Planned Evaluation):
- **Accuracy, Precision, Recall, F1 Score:** Will be used to assess the system’s ability to correctly identify true anomalies versus false positives/negatives once data is available.
- **Detection Latency:** Targeting rapid detection, measured as the time from anomaly occurrence to alert generation. Evaluation metrics may include tool trajectory average score and response match score.
### Predictive Maintenance(Planned Evaluation):
- **Prediction Accuracy:** The system will be evaluated on its ability to forecast equipment failures before they occur, minimizing unplanned downtime.
### Guidance Effectiveness(Projected Impact):
- **Task Completion Rate:** Aim for at least 15% of repairs to be completed successfully using AR guidance, especially by less experienced technicians.
- **Error Reduction:** Expect a measurable decrease in maintenance errors after implementation.
- **Time-to-Resolution:** Targeting a reduction in average repair time compared to current baseline processes.
## Operational Metrics(Anticipated Outcomes):

- **Downtime Reduction:** Percentage decrease in unplanned downtime across monitored equipment.
- **Mean Time to Repair (MTTR):** Improvement in repair speed over traditional maintenance methods.
- **User Adoption Rate:** Percentage of technicians regularly utilizing the system.
- **Notification Response Time:** Time from alert issuance to technician acknowledgment.
## Cost Structure & Revenue Model:

### Cost Structure:
- Cloud compute and storage (AI inference, data logs).
- AR headset hardware (Meta Quest 3).
- Integration and support.
### Revenue Model:
- SaaS subscription per site or per device.
- Tiered pricing based on feature set (basic monitoring vs. full AR guidance).
- Optional professional services for integration and training.
## KPIs:
- Reduction in downtime and maintenance costs.
- Increase in first-time fix rate.
- Technician training time reduction.
- Compliance with safety protocols.

# Execution Plan
**Deployment & Distribution:**
- Deploy an integrated system combining Jira dashboards for real-time machine health monitoring, automated ticketing, and maintenance analytics. 
- Utilize the B5META Mixed Reality Dashboard to prioritize alerts, manage technician tasks, and track expertise. Deliver immersive, step-by-step AR repair guidance via Meta Quest 3 headsets for hands-free, efficient maintenance. 
- Ensure seamless IoT sensor data integration with AI-driven anomaly detection and predictive insights. 
- Provide comprehensive analytics and compliance tools to maximize uptime and safety.

# Data Ingestion & Flow
![Alt text](https://github.com/user-attachments/assets/7decd02c-287c-4da0-9d7c-aaf2cfeba928)
![Alt text](https://github.com/user-attachments/assets/84053662-4f1a-4925-aec5-2fdd797618cb)
- Continuous ingestion of sensor, visual, and manual data
- Centralized knowledge base for up-to-date context
- Real-time feedback loop for anomaly detection, prediction, and guidance

# Under the Hood: Our Technology Stack with Modern MCP Tools Box
- Our solution harnesses a modern technology stack built around the ** Model Context Protocol (MCP)** to enable seamless, context-aware industrial maintenance.
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

# How to Run This Project on Meta Quest 3

1. Clone the Repo
   Clone the project to your local machine:
   git clone https://github.com/capgcat/capgineered-meta-xr-ai-agents-.git

2. Open the Project in Unity
   Open Unity Hub → Click Add → Select the /ui/mixed-reality/meta-machine-xr-ai-agent folder → Open with Unity 2022.3 LTS (or version used in this project).

3. Switch to Android Platform
   Go to File → Build Settings → Select Android → Click Switch Platform.

4. Install Meta XR SDK
   Open Window → Package Manager → Add Meta XR All-in-One SDK via Git URL:
   https://github.com/MetaQuestDeveloper/Unity-MetaQuest-SDK.git

5. Enable XR Plugin & Oculus Support
   Go to Edit → Project Settings → XR Plug-in Management → Enable Oculus under Android tab.

6. Set Android Build Settings
   In Player Settings → Other Settings:
   - Set Package Name (e.g., com.company.app)
   - Set Minimum API Level to 29
   - Set Target API Level to 33 or 34

7. Configure Oculus Features (if used)
   In Project Settings → Oculus → Quest Features, enable Hand Tracking, Passthrough, or other required capabilities.

8. Connect Quest 3 in Developer Mode
   - Enable Developer Mode using Meta Quest mobile app
   - Connect Quest 3 via USB
   - Accept USB Debugging prompt inside the headset

9. Build and Deploy to Headset
   Go to File → Build Settings → Build and Run → Choose the connected Quest 3 device.

10. Launch and Test in Headset
    Once installed, the app will auto-launch. Put on your headset and enjoy testing your experience!


# Safety and Security
- Role-based access control for dashboards and agent actions
- Data encryption in transit and at rest
- Audit logs for all automated actions and recommendations

# Live Demo Walkthrough
See It In Action:

Watch as our system detects an anomaly, suggests a self-healing action, and provides real-time XR guidance to a technician, while SOC analysts receive proactive notifications and incident coordination.

[![Capgineered Agents](https://img.youtube.com/vi/nsl6nqciiXs/0.jpg)](https://www.youtube.com/watch?v=nsl6nqciiXs "Capgineered Agents")


# What’s Next: Our Vision
- Deeper integration with legacy industrial systems
- Expanded XR/VR capabilities for remote collaboration
- Continuous learning from incident data to improve agent intelligence

# Contributors
