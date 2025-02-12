import os

from fastapi import APIRouter, Request, Response
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/support", tags=["support"])
templates = Jinja2Templates(directory="app/view")


@router.get("/")
async def support(request: Request):
    return templates.TemplateResponse("support.html", {"request": request})