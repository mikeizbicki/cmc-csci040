'''
Starts a hello world webserver.
'''

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return 'hello <b>world</b>'

if __name__ == '__main__':
    uvicorn.run("webserver:app", host='127.0.0.1', port=8080, reload=True)