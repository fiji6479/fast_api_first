from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps import exception_handlers
from apps.mainapp import api_router

def create_app():
    app = FastAPI(exception_handlers=exception_handlers)
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.mount('/media', StaticFiles(directory='media'), name='media')
    app.include_router(api_router)
    return app

