from datetime import datetime as dt
from fastapi import Request
from fastapi.responses import HTMLResponse,JSONResponse,FileResponse
from server_app import *
from server_app.models import *
from server_app.nav_bar import nav_context,refresh_context
from server_app.misc import *
from server_app.diary import get_diary_context_search_managed

page_context = {'mode':'dark' if(18 <= dt.now().time().hour <= 24 or 0 <= dt.now().time().hour <= 8) else 'light'}
common_context = {**nav_context,**page_context}

# root
@app.get('/',response_class=HTMLResponse)
@app.get(f'/{DiaryEntry.url}/',response_class=HTMLResponse)
async def root(request: Request, search: str | None = None):
    refresh_context()
    diary = get_diary_context_search_managed(diary_context=DiaryEntry.context_no,search=search,nav_context=nav_context)
    
    return templates.TemplateResponse(
        request=request, 
        name=template_home, 
        context={**common_context,**diary},
    )

@app.get(f'/{Task.url}/',response_class=HTMLResponse)
async def root(request: Request, search: str | None = None):
    refresh_context()
    diary = get_diary_context_search_managed(diary_context=Task.context_no,search=search,nav_context=nav_context)

    return templates.TemplateResponse(
        request=request, 
        name=template_home, 
        context={**common_context,**diary},
    )

@app.get(f'/{Event.url}/',response_class=HTMLResponse)
async def root(request: Request, search: str | None = None):
    refresh_context()
    diary = get_diary_context_search_managed(diary_context=Event.context_no,search=search,nav_context=nav_context)

    return templates.TemplateResponse(
        request=request, 
        name=template_home, 
        context={**common_context,**diary},
    )

@app.get(f'/{Note.url}/',response_class=HTMLResponse)
async def root(request: Request, search: str | None = None):
    refresh_context()
    diary = get_diary_context_search_managed(diary_context=Note.context_no,search=search,nav_context=nav_context)
    
    return templates.TemplateResponse(
        request=request, 
        name=template_home, 
        context={**common_context,**diary},
    )

@app.get('/diary/',response_class=HTMLResponse)
async def root(request: Request):
    refresh_context()
    diary = read_file('diary.txt')
    return templates.TemplateResponse(
        request=request, 
        name=template_home_diary, 
        context={**common_context,'data':'\n'.join(diary)},
    )

@app.post('/diary/update/',response_class=JSONResponse)
async def root(du:DiaryUpdate): 
    refresh_context()
    if(du.password == 'mypass'):
        with open('diary.txt','w') as f:
            f.write(du.data)
    return {'result':True}

@app.get('/help/',response_class=HTMLResponse)
async def root(request: Request):
    refresh_context()
    return templates.TemplateResponse(
        request=request, 
        name=template_home_help, 
        context={**common_context},
    )