from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.auth.service import get_admin_by_token


router = APIRouter()

templates = Jinja2Templates(directory='app/view')

@router.get('/admin')
async def login_page(request: Request, user=Depends(get_admin_by_token)):
    return templates.TemplateResponse('admin.html', {'request': request})