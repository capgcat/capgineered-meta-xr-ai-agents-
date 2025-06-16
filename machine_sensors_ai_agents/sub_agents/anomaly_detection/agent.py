from google.adk.agents import Agent

from .prompt import ANOMALY_AGENT_INSTRUCTION, return_instructions_root
from .tools import toolbox_tools  # Import the updated toolbox tools
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag
import os
from dotenv import load_dotenv
load_dotenv()

from machine_sensors_ai_agents.sub_agents.rag_agent.agent import rag_agent

ask_vertex_retrieval = VertexAiRagRetrieval(
    name='retrieve_rag_documentation',
    description=(
        'Use this tool to retrieve documentation and reference materials for the question from the RAG corpus,'
    ),
    rag_resources=[
        rag.RagResource(
            # please fill in your own rag corpus
            # here is a sample rag corpus for testing purpose
            # e.g. projects/123/locations/us-central1/ragCorpora/456
            rag_corpus=os.environ.get("RAG_CORPUS")
        )
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6,
)

ask_agent = Agent(
    model='gemini-2.0-flash-001',
    name='rag_agent',
    instruction=return_instructions_root(),
    tools=[
        ask_vertex_retrieval,
    ]
)

anomaly_agent = Agent(
    name="anomaly_agent",
    model="gemini-2.0-flash",
    description="Identifies abnormal patterns and deviations in real-time industrial sensor data.",
    instruction=ANOMALY_AGENT_INSTRUCTION,
    sub_agents=[ask_agent],  # Include the rag_agent for RAG capabilities
    tools=[*toolbox_tools], # Use the new list of ADK tools
)