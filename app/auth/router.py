import uuid
import os
import shutil

from fastapi import APIRouter, Request, Response, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Optional
from starlette.exceptions import HTTPException
from datetime import date
from app.auth.service import create_token, hash_password


router = APIRouter()

templates = Jinja2Templates(directory='app/view')


@router.get('/login')
async def login_page(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


@router.get('/logout')
async def logout(request: Request):
    pass


@router.get('/registration')
async def register_page(request: Request):
    return templates.TemplateResponse('registration.html', {'request': request})


@router.get('/login/token')
async def login_with_token(request: Request):
    return templates.TemplateResponse('login_with_token.html', {'request': request})


@router.get('/successfully')
async def successful_page(request: Request):
    return templates.TemplateResponse('successful.html', {'request': request})
