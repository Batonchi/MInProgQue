from fastapi import FastAPI, Request, Response
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from database import create_database, rcache


create_database()


app = FastAPI()
templates = Jinja2Templates(directory="templates")
# включение роутеров

