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
        return f"{e}"


def split_templates(cover_letter):
    if "**Cover Letter 2:**" in cover_letter:
        parts = cover_letter.split("**Cover Letter 2:**")
        cover_letter_1 = parts[0].strip().replace("**Cover Letter 1:**", "").strip()
        cover_letter_2 = parts[1].strip()
    else:
        # fallback if the expected structure is not found
        cover_letter_1 = cover_letter
        cover_letter_2 = ""

    return {
        "cover_letter_1": cover_letter_1,
        "cover_letter_2": cover_letter_2
    }



# Create an instance of the FastAPI class
app = FastAPI()
origins=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",  # Localhost version for React app

]

# Adding CORS middleware to allow requests from any origin (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class InputData(BaseModel):
    job_desc: str
    resume: str

# #test connection
@app.get("/test_connection")
async def test_connection():
    return {"status": "Connection to FastAPI is working!"}

@app.post("/send_text")
async def receive_text(data: InputData):
    job_Desc = data.job_desc
    resume = data.resume
    #reply from AI stored in cover_letters
    #sends 2 templates together
    cover_letters = model_reply(job_Desc,resume)

    #split the templates and store them in a dictionary to return to React
    return split_templates(cover_letters)



#command to start backend
#uvicorn main:app --reload


