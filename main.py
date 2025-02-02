from fastapi import FastAPI, Request, Response, HTTPException
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from database import create_database, rcache


create_database()


app = FastAPI()
templates = Jinja2Templates(directory="app/view")


app.mount('/static', StaticFiles(directory='app/view/static'))
# включение роутеров


@app.exception_handler(HTTPException):
async def exception_handel(request: Request, exc):
    code = exc.__dict__['status_code']
    # сдклать обработку ошибок и вывод окон


@app.get("/error")
async def error(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})


@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

