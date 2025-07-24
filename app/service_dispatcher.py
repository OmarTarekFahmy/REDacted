from fastapi import HTTPException
import sanitizer, openai_service, email_alert


'''
This is a middle layer between the FastAPI app and the services. It sanitizes the text (always done) and routes the JSON to the 
correct service based on the type.
'''

async def process(data, user_ip):
    
    # Obtain type and text
    type = data.get("type", "")
    text = data.get("text", "")

    # Raise HTTP Exception if either is empty
    if not type or not text:
        raise HTTPException(400, "Type and Text fields cannot be empty.")
    
    # Sanitize Text
    sanitized_text = sanitizer.sanitize_all(text)

    if text != sanitized_text:
        email_alert.send_alert_email(user_ip)


    # Match against each type and route to corresponding service. General type does not require routing since text has been sanitized 
    match type:
        case "general":
            data.pop("text")
            data["sanitized_text"] = sanitized_text
            return data
        
        case "summarize":

            summarized_text = openai_service.summarize(text)
            sanitized_summarized_text = sanitizer.sanitize_all(summarized_text)
            data.pop("text")
            data["summarized_text"] = sanitized_summarized_text
            
            return data            
        case "translate":
            target_language = data.get("target_language", "")

            if not target_language:
                raise HTTPException(400, "Target language must not be empty when translating.")
            
            translated_text = openai_service.translate(sanitized_text, target_language)

            data.pop("text")
            data["translated_text"] = translated_text
            
            return data

            pass
        case _:
            raise HTTPException(400, "Bad Type")
