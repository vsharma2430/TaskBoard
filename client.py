import uvicorn
from multiprocessing import cpu_count

if (__name__ == '__main__'):
    #uvicorn.run('server_app.main:app',reload=True)
    uvicorn.run('server_app.main:app', host='0.0.0.0',reload=True, port=8007,workers=cpu_count()*2+1)