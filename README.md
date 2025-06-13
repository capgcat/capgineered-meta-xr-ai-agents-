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
