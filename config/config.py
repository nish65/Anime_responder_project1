import os
from dotenv import load_dotenv

load_dotenv() # These loading all the component present in the .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # fetching the ("GROQ_API_KEY") from .env  
MODEL_NAME = "llama-3.1-8b-instant"  #Model name of the GROQ_API