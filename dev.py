import uvicorn

if (__name__ == '__main__'):
    uvicorn.run('server_app.main:app',reload=True)

    