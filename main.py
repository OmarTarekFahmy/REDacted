from fastapi import FastAPI, Request
from fastapi.responses import Response, JSONResponse
import spacy
import re


app = FastAPI()
nlp = spacy.load("en_core_web_sm")


#Sanitizes: Mail, Phone, IPs
def sanitize_regex(text: str) -> str:
    # Regex for IPv4
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    # Regex for IPv6
    ipv6_pattern = r'\b(?:[A-Fa-f0-9:]+:+)+[A-Fa-f0-9]+\b'
    
    # Regex for email
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    #Regex for phone
    phone_pattern = r'(?:\+?20|0)1[0-5]\d{8}'

    # Replace matches with placeholders
    text = re.sub(ipv4_pattern, '<REDACTED IPv4>', text)
    text = re.sub(ipv6_pattern, '<REDACTED IPv6>', text)
    text = re.sub(email_pattern, '<REDACTED EMAIL>', text)
    text = re.sub(phone_pattern, '<REDACTED PHONE NUMBER>', text)

    return text

def sanitize_names(text: str):
    doc = nlp(text)
    sanitized = text
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            sanitized = sanitized.replace(ent.text, "<REDACTED NAME>")
    return sanitized

def sanitize_all(text: str):
    text = sanitize_names(text)
    text = sanitize_regex(text)
    return text


@app.post("/sanitize")
async def sanitization_endpoint(request: Request):

    data = await request.json()

    original_text = data.get("Text", "")
    print(original_text)

    sanitized_text = sanitize_all(original_text)

    data.pop("Text", None)
    data['sanitized_text'] = sanitized_text

    print(sanitized_text)

    return JSONResponse(content=data)   

    

