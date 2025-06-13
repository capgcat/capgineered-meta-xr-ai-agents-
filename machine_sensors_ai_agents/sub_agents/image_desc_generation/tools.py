from google.cloud import storage
import vertexai
from vertexai.generative_models import GenerativeModel, Image
from google.adk.tools import FunctionTool, ToolContext
from dotenv import load_dotenv
import os


load_dotenv()

# Load environment variables
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
MODEL = "gemini-2.5-pro-preview-05-06"

# --- GCS Tool ---
def get_image_from_gcs(image_url: str, tool_context: ToolContext) -> str:
    """
    Retrieves an image from a Google Cloud Storage URI (gs://...) and saves it temporarily.
    Returns the local path to the downloaded image.
    """
    if not image_url or not image_url.startswith("gs://"):
        print(f"Invalid GCS URL provided: {image_url}")
        return None

    # Parse bucket and object name from the gs:// URI
    path_parts = image_url[len("gs://"):].split("/", 1)
    bucket_name = path_parts[0]
    object_name = path_parts[1] if len(path_parts) > 1 else ""

    storage_client = storage.Client()

    # Determine a temporary local path
    temp_local_path = f"/tmp/{object_name.split('/')[-1]}" 
    # Consider more robust temporary file handling for production

    try:
        blob = storage_client.bucket(bucket_name).blob(object_name)
        if not blob.exists():
             raise FileNotFoundError(f"Object gs://{bucket_name}/{object_name} not found.")

        blob.download_to_filename(temp_local_path)

        print(f"Image {object_name} downloaded to {temp_local_path}")
        return temp_local_path
    except Exception as e:
        print(f"Error downloading image from GCS: {e}")
        return None

# --- Image Description Tool ---
def describe_image_with_gemini(image_local_path: str, tool_context: ToolContext) -> str:
    """
    Generates a description for a local image file using Vertex AI Gemini.
    """
    if not image_local_path:
        return "Error: No image path provided for description."

    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = GenerativeModel(MODEL) # Or other suitable Gemini vision model

    try:
        with open(image_local_path, "rb") as f:
            image_bytes = f.read()
        image = Image.from_bytes(image_bytes)

        responses = model.generate_content([image, "Describe this image in detail, focusing on key objects, colors, and overall scene. Provide a concise summary."])
        
        # Extract the text from the response
        description = ""
        for part in responses.candidates[0].content.parts:
            description += part.text
        return description
    except Exception as e:
        print(f"Error generating image description: {e}")
        return f"Error: Could not describe image. {e}"
    finally:
        # Clean up the temporary file
        import os
        if os.path.exists(image_local_path):
            os.remove(image_local_path)
            print(f"Cleaned up temporary file: {image_local_path}")



# Wrap your custom functions as ADK FunctionTools
gcs_reader_tool = FunctionTool(get_image_from_gcs)
gemini_describer_tool = FunctionTool(describe_image_with_gemini)
