import os
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from openai


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

#test connection
@app.post("/items")
async def create_item(request: Request):
    # Read plain text from the request body
    desc_input = await request.body()
    desc_input = desc_input.decode("utf-8")  # Convert bytes to string
    return {"message": f"Received: {desc_input}"}




# if __name__ =="__main__":
#     uvicorn.run(app,host = "0.0.0.0",port=8000)