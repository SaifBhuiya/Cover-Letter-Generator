import os
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv,find_dotenv
import prompts
from pydantic import BaseModel
from config import MODEL_NAME, TEMPERATURE, MAX_TOKENS, OPENAI_BASE_URL

#load the .env file for LLM Integration Token
load_dotenv(find_dotenv())
client=OpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=os.environ.get('GITHUB_TOKEN'),
)


#Function to use LLM Model
def model_reply(job_Desc, resume):
    try:
        system_message = prompts.system_message
        prompt = prompts.generate_prompt(job_Desc, resume)
        messages = [
            {"role":"system","content": system_message},
            {"role":"user","content": prompt}
        ]
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error generating reply: {e}")
        return "Error generating cover letter."






# Create an instance of the FastAPI class
app = FastAPI()
origins=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",  # Localhost version for React app

]

# Adding CORS middleware to allow requests from any origin (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # You can replace "*" with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class InputData(BaseModel):
    job_desc: str
    resume: str

# #test connection
@app.post("/send_text")
async def receive_text(data: InputData):
    job_Desc = data.job_desc
    resume = data.resume

    print(model_reply(job_Desc,resume))
    return {
        "job_description_received": data.job_desc,
        "resume_received": data.resume
    }


#command to start backend
#uvicorn main:app --reload


