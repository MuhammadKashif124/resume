from fastapi import FastAPI, HTTPException
import google.generativeai as genai
from google.generativeai import GenerativeModel

# Configure the GenerativeAI API key
genai.configure(api_key="AIzaSyDn-Ik881z2rdLz-KOEMwo3v0fauL-Bnx0")

# Set up the model configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Initialize the GenerativeAI model
model = GenerativeModel(model_name="gemini-1.0-pro",
                        generation_config=generation_config,
                        safety_settings=safety_settings)

# Create a FastAPI instance
app = FastAPI()

# Define a route to handle user input and generate response
@app.post("/generate_response/")
async def generate_response(prompt: str):
    try:
        # Generate content based on the prompt
        response = model.generate_content(prompt)

        # Check if the response has text available
        if response.text:
            return {"response": response.text}
        else:
            raise HTTPException(status_code=500, detail="Failed to generate response. No text available.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate response: {str(e)}")

# Define a route for ranking some data
@app.post("/rank_data/")
async def generate_response(prompt: str):
    try:
        # Generate content based on the prompt
        response = model.generate_content(prompt)

        # Check if the response has text available
        if response.text:
            return {"response": response.text}
        else:
            raise HTTPException(status_code=500, detail="Failed to generate response. No text available.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate response: {str(e)}")
# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
