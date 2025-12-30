import os
from dotenv import load_dotenv

# Common setup for AI Agent projects
def load_env_variables():
    load_dotenv()
    print("Environment variables loaded.")

def get_openai_api_key():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

if __name__ == "__main__":
    load_env_variables()
