import fastapi
from fastapi import HTTPException
import requests
import openai

app = fastapi.FastAPI()
OPENAI_API_KEY = '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'

@app.post("/generate_resume/")
async def generate_resume(user_data: str):
    # Call OpenAI's chat completion endpoint to generate resume
    response = openai.ChatCompletion.create(
        'model': 'gpt-4',
        'prompt': user_data,
        'max_tokens': 150,
    )

    if response.status_code == 200:
        data = response.json()
        resume = data.get('choices', [{'text': 'No response from API'}])[0]['text']
        return {"resume": resume}
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to generate resume")

@app.post("/generate_cover_letter/")
async def generate_cover_letter(user_data: str):
    # Call OpenAI's chat completion endpoint to generate cover letter
    response = requests.post('https://api.openai.com/v1/completions', json={
        'model': 'gpt-4',
        'prompt': user_data,
        'max_tokens': 150,
    }, headers={
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    })

    if response.status_code == 200:
        data = response.json()
        cover_letter = data.get('choices', [{'text': 'No response from API'}])[0]['text']
        return {"cover_letter": cover_letter}
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to generate cover letter")

@app.post("/rank_resume/")
async def rank_resume(resume_data: str):
    # Perform some ranking algorithm based on resume data
    # For simplicity, let's just count the number of characters
    ranking = len(resume_data)
    return {"ranking": ranking}
