from fastapi import Request, APIRouter, HTTPException
from jinja2 import Template
from starlette.templating import Jinja2Templates
from app.pages.service import PageService
from app.auth.service import get_admin_by_token


router = APIRouter(
    prefix="/pages",
    tags=["task_pages"],
)

templates = Jinja2Templates(directory="app/view")


@router.get('')
async def all_task_page(request: Request):
    return templates.TemplateResponse("all_tasks.html", {"request": request})


@router.get('/{page_id}')
async def page(request: Request, page_id: str):
    pass