import os
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv,find_dotenv


#load the .env file
load_dotenv(find_dotenv())
client=OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ.get('GITHUB_TOKEN'),
)

model = "gpt-4o"
temperature = 1
max_tokens = 4096
topic = ""

book = ""

# system_message = prompts.system_message
# prompt = prompts.generate_prompt (book, topic)

messages = [
    {"role":"system","content": "You are an HR Hiring Manager at a renowed Tech Company. You have years of experience under your belt reviewing the cover letters of thousands of applicants"},
    {"role":"user","content": "Give me 2 basic templates for a cover letter"}
]
def get_reply():
    completion= client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return completion.choices[0].message.content

print(get_reply())

# Create an instance of the FastAPI class
# app = FastAPI()
# origins=[
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",  # Localhost version for React app
#
# ]
#
# # Adding CORS middleware to allow requests from any origin (for development purposes)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,  # You can replace "*" with specific domains in production
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )






# #test connection
# @app.post("/items")
# async def create_item(request: Request):
#     # Read plain text from the request body
#     desc_input = await request.body()
#     desc_input = desc_input.decode("utf-8")  # Convert bytes to string
#     return {"message": f"Received: {desc_input}"}
#
