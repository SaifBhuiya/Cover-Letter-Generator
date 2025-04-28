import os

MODEL_NAME = "gpt-4o"
TEMPERATURE = 1
MAX_TOKENS = 4096
OPENAI_BASE_URL = "https://models.inference.ai.azure.com"
#not used
OPENAI_API_KEY = os.getenv("GITHUB_TOKEN")