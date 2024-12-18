import os
import signal
from fastapi import FastAPI, Request,Response
from fastapi.responses import HTMLResponse,JSONResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from logging import getLogger


app = FastAPI()
logger = getLogger('uvicorn.error')

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')
template_home = 'home.html'
template_home_diary = 'diary_home.html'
template_home_help = 'help_home.html'

#favicon and images
favicon_path = f'static/images/favicon.ico'
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

#start-stop
def start():
    return Response(status_code=200, content='Server started')

def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)
    return Response(status_code=200, content='Server shutting down...')

app.add_api_route('/start', start, methods=['GET'])
app.add_api_route('/shutdown', shutdown, methods=['GET'])