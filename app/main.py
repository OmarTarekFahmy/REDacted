from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
import  service_dispatcher
from fastapi.middleware.cors import CORSMiddleware



'''
This is the FastAPI app. It includes a single endpoint at path "/". This endpoint handles all requests by sending the data to
the service dispatcher. The service dispatcher checks the json type (general, summarize, translate) and handles each case.

This data is then returned to main.py and returned as the JSON response.

'''

app = FastAPI()

# Allow requests from your frontend (adjust port if different)
origins = [
    "http://localhost:8080",  # Vite default port
    "http://127.0.0.1:8080",  # Also valid
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def trigger(request: Request):
 
    user_ip = request.client.host
    data = await request.json()
    data = await service_dispatcher.process(data, user_ip)

    return JSONResponse(data)


@app.get("/string")
async def test():
 
    retData = {"response": "Hello from server"}
    return "Test String"

@app.get("/json")
async def test():
 
    retData = {"response": "Hello from server"}
    return retData

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def test():
    return "<h1>Hello from server</h1>"



