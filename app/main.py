from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import  service_dispatcher

'''
This is the FastAPI app. It includes a single endpoint at path "/". This endpoint handles all requests by sending the data to
the service dispatcher. The service dispatcher checks the json type (general, summarize, translate) and handles each case.

This data is then returned to main.py and returned as the JSON response.

'''

app = FastAPI()


@app.post("/")
async def trigger(request: Request):


    data = await request.json()
    data = await service_dispatcher.process(data)

    return JSONResponse(data)


    

