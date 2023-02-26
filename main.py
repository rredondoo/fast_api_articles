from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
# from exceptions import StoryExcepction
from fastapi.responses import JSONResponse


app = FastAPI()


app.get('/hello')
def index():
    return {'message': 'hello world!'}


# app.include_router(user.router)
# app.include_router(user.router)
# app.include_router(user.router)
# app.include_router(user.router)


app.add_middleware(
    CORSMiddleware,
    allow
)