from datetime import datetime as dt
from fastapi import FastAPI, Request,Response
from fastapi.responses import HTMLResponse,JSONResponse,FileResponse
from server_app import *
from server_app.models import *
from server_app.nav_bar import nav_context
from server_app.misc import *
from server_app.diary import get_diary_context

# root
@app.get('/',response_class=HTMLResponse)
@app.get('/task/',response_class=HTMLResponse)
@app.get('/event/',response_class=HTMLResponse)
async def root(request: Request):
    diary = get_diary_context()
    return templates.TemplateResponse(
        request=request, 
        name=template_home, 
        context={**nav_context,**diary},
    )