# REDacted

This project is a FastAPI-based microservice that provides three main functionalities:

1. **Sanitization**  
   - Removes sensitive information from text (names, emails, IP addresses, Egyptian phone numbers).

2. **Translation**  
   - Translates text into a target language using OpenAI's GPT models.

3. **Summarization**  
   - Generates a concise summary of the given text using OpenAI's GPT models.
  
4. **Alerts**  
   - Send an email alert to target address alerting that a user has entered sensitive information alongside user's IP address

---

## 🚀 Features
- RESTful API built with FastAPI.
- Asynchronous request handling for scalability.
- Integration with OpenAI API (`gpt-3.5-turbo` for cost-effective processing).
- Environment variable management via `.env`.

---

## 🛠 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/OmarTarekFahmy/REDacted.git
cd REDacted
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a .env file in the project root and add:

```bash
OPENAI_API_KEY=your_openai_api_key_here
ALERT_EMAIL_SENDER=sender_email_here
ALERT_EMAIL_RECEIVER=receiver_email_here
ALERT_EMAIL_PASSWORD=receiver_password_here
```

### ▶️ Running the Application
```bash
cd app
uvicorn main:app --reload
```

### Supported Actions

| `type` value | Description                          | Required Fields           |
| ------------ | ------------------------------------ | ------------------------- |
| `general`   | Removes sensitive info from text     | `text`                    |
| `translate`  | Translates text into target language after sanitization | `text`, `target_language` |
| `summarize`  | Summarizes text after sanitization                      | `text`                    |


### ✅ Example Requests

#### 1. Sanitization
```bash
curl -X POST "http://localhost:8000/" \
-H "Content-Type: application/json" \
-d '{
  "type": "general",
  "text": "John Doe accessed the server at IP 192.168.1.10 and emailed admin@example.com."
}'
```
#### Response Example
```bash
{
  "status": "success",
  "result": {
    "sanitized_text": "<REDACTED NAME> accessed the server at IP <REDACTED IPv4> and emailed <REDACTED EMAIL>."
  }
}
```

#### 2. Translation
```bash
curl -X POST "http://localhost:8000/" \
-H "Content-Type: application/json" \
-d '{
  "type": "translate",
   "target_language": "French",
  "text": "Hello, how are you?"
}'
```
#### Response Example
```bash
{
  "status": "success",
  "result": {
    "translated_text": "Bonjour, comment allez-vous ?"
  }
}
```
#### 3. Summarization
```bash
curl -X POST "http://localhost:8000/" \
-H "Content-Type: application/json" \
-d '{
  "type": "summarize",
  "text": "FastAPI is a modern Python framework for building APIs. It offers speed and ease of development through async support."
}'
```
#### Response Example
```bash
{
  "status": "success",
  "result": {
    "summary": "FastAPI is a fast, modern Python API framework with async support."
  }
}

```

### ✅ For quick testing, you can also use Postman:

Set method: POST

URL: http://localhost:8000/

Body: raw → JSON

Add required fields (type, text, target_language if needed).


