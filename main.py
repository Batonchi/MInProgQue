from fastapi import FastAPI, Request, Response, HTTPException
from pip._internal.network import auth
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from database import create_database, rcache
from app.auth.router import router as auth_router


create_database()


app = FastAPI()
templates = Jinja2Templates(directory="app/view")

app.include_router(auth_router)
app.mount('/static', StaticFiles(directory='app/view/static'))
# включение роутеров


@app.exception_handler(HTTPException)
async def exception_handel(request: Request, exc):
    code = exc.__dict__['status_code']
    # сдклать обработку ошибок и вывод окон


@app.get("/error")
async def error(request: Request):
    return templates.TemplateResponse("error.html", {"request": request, })


@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("sources.html", {"request": request})

