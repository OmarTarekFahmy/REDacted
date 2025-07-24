# REDacted

This project is a FastAPI-based microservice that provides three main functionalities:

1. **Sanitization**  
   - Removes sensitive information from text (names, emails, IP addresses, Egyptian phone numbers).

2. **Translation**  
   - Translates text into a target language using OpenAI's GPT models.

3. **Summarization**  
   - Generates a concise summary of the given text using OpenAI's GPT models.

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
cd text-processing-service
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

```

### ▶️ Running the Application
```bash
cd app
uvicorn main:app --reload
```




