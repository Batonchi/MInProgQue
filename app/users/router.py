import os

from fastapi import APIRouter, Request, Response
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/users", tags=["users"])
templates = Jinja2Templates(directory="app/view")


@router.get("/profile")
async def profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})