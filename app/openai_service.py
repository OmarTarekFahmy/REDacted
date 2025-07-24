from openai import OpenAI
from fastapi import HTTPException
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def translate(text: str, target_language: str) -> str:
    

    prompt = f"Translate the following text into {target_language}:\n\n{text}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Cheapest general-purpose chat model
            messages=[
                {"role": "system", "content": "You are a professional translator. Respond only with the translated text."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,  # Low randomness for accurate translation
        )
        
        return response.choices[0].message.content.strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")