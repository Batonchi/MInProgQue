from fastapi import FastAPI, Request, Response, HTTPException
from pip._internal.network import auth
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from database import create_database
from app.auth.router import router as auth_router
from app.pages.router import router as page_router
from app.support.router import router as support_router
from app.users.router import router as user_router


create_database()


app = FastAPI()
templates = Jinja2Templates(directory="app/view")

app.include_router(auth_router)
app.include_router(page_router)
app.include_router(support_router)
app.include_router(user_router)
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


@app.get("/contact")
async def home(request: Request):
    return templates.TemplateResponse("contact_drop.html", {"request": request, "email_address": 'gkok.gkok@yandex.ru', "number_of_phone": '+7 (927) 378 25-74', "tg_name": 'Batinchi'})


@app.get("/rules")
async def home(request: Request):
    return templates.TemplateResponse("rules.html", {"request": request})


@app.get("/sources")
async def home(request: Request):
    return templates.TemplateResponse("sources.html", {"request": request})

