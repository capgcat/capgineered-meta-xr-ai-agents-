To upload a different PDF from a URL: a. Open the /shared_libraries/rag_agents_data.py file. b. Modify the following variables at the top of the script:

# --- Please fill in your configurations ---
# ... project and location are read from .env ...
CORPUS_DISPLAY_NAME = "Your_Corpus_Name"  # Change as needed
CORPUS_DESCRIPTION = "Description of your corpus" # Change as needed
PDF_URL = "https://path/to/your/document.pdf"  # URL to YOUR PDF document
PDF_FILENAME = "your_document.pdf"  # Name for the file in the corpus
# --- Start of the script ---
c. Run the script:

python /shared_libraries/rag_agents_data.py