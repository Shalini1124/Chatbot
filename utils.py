import os
from dotenv import load_dotenv

load_dotenv()

def load_api_key():
    """Loads the API key from .env file."""
    return os.getenv("HUGGINGFACE_API_KEY")
