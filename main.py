import uvicorn

from fastapi import FastAPI, Request, Response, HTTPException
from pip._internal.network import auth
from starlette.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from app.auth.router import router as auth_router
from app.pages.router import router as page_router
from app.support.router import router as support_router
from app.users.router import router as user_router
from app.admin.router import router as admin_router


app = FastAPI()
templates = Jinja2Templates(directory="app/view")

# включение роутеров
app.include_router(auth_router)
app.include_router(page_router)
app.include_router(support_router)
app.include_router(user_router)
app.include_router(admin_router)

app.mount('/static', StaticFiles(directory='app/view/static'))


@app.middleware("http")
async def error_handler(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 409:
        return RedirectResponse(url='/login', status_code=302)
    if response.status_code == 403:
        return templates.TemplateResponse("error.html", {"request": request, "error_message": "У вас нет доступа!"})
    elif response.status_code == 404:
        return templates.TemplateResponse("error.html", {"request": request, "error_message": "Страница не найдена((("})
    return response



# @app.exception_handler(HTTPException)
# async def exception_handel(request: Request, exc):
#     code = exc.__dict__['status_code']
#     # сдклать обработку ошибок и вывод окон


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

@app.get('/home')
async def home(request: Request):
    return templates.TemplateResponse("edit_article.html", {"request": request})


    