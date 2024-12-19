from datetime import datetime as dt
from fastapi import Request
from fastapi.responses import HTMLResponse,JSONResponse,FileResponse
from server_app import *
from server_app.models import *
from server_app.nav_bar import nav_context
from server_app.misc import *
from server_app.diary import get_diary_context

page_context = {'mode':'dark' if(18 <= dt.now().time().hour <= 24 or 0 <= dt.now().time().hour <= 8) else 'light'}
common_context = {**nav_context,**page_context}

# root
@app.get('/',response_class=HTMLResponse)
async def root(request: Request):
    diary = get_diary_context()
    return templates.TemplateResponse(
        request=request, 
        name=template_home, 
        context={**common_context,**diary,'diary_context':0},
    )

@app.get('/task/',response_class=HTMLResponse)
async def root(request: Request):
    diary_context = 1
    diary = get_diary_context(diary_context)

    return templates.TemplateResponse(
        request=request, 
        name=template_home, 
        context={**common_context,**diary,'diary_context':diary_context},
    )

@app.get('/event/',response_class=HTMLResponse)
async def root(request: Request):
    diary_context = 2
    diary = get_diary_context(diary_context)
    return templates.TemplateResponse(
        request=request, 
        name=template_home, 
        context={**common_context,**diary,'diary_context':diary_context},
    )

@app.get('/note/',response_class=HTMLResponse)
async def root(request: Request):
    diary_context = 3
    diary = get_diary_context(diary_context)
    return templates.TemplateResponse(
        request=request, 
        name=template_home, 
        context={**common_context,**diary,'diary_context':diary_context},
    )

@app.get('/diary/',response_class=HTMLResponse)
async def root(request: Request):
    diary = read_file('diary.txt')
    return templates.TemplateResponse(
        request=request, 
        name=template_home_diary, 
        context={**common_context,'data':'\n'.join(diary)},
    )

@app.post('/diary/update/',response_class=JSONResponse)
async def root(de:DiaryString): 
    with open('diary.txt','w') as f:
        f.write(de.data)
    return {'result':True}

@app.get('/help/',response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name=template_home_help, 
        context={**common_context},
    )