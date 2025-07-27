from openai import OpenAI
from fastapi import HTTPException
import os
from dotenv import load_dotenv

'''
This service handles all calls to OpenAI regarding translation and summarization using gpt-3.5-turbo for low cost
'''

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def translate(text: str, target_language: str) -> str:
    

    prompt = f"Translate the following text into {target_language}:\n\n{text}"

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",  # Cheapest general-purpose chat model
            messages=[
                {"role": "system", "content": "You are a professional translator. Respond only with the translated text."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,  # Low randomness for accurate translation
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")
    
def summarize(text: str) -> str:
    if not text:
        raise HTTPException(status_code=400, detail="Text must not be empty for summarization.")

    prompt = f"Summarize the following text in a clear, concise way. If you see anything redacted, do not remove it and keep the redacted text:\n\n{text}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text accurately, but does not remove any mention of redacted text or IPs or mails etc."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Lower for more factual summaries
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summarization failed: {str(e)}")