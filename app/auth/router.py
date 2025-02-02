import uuid
import os
import shutil
from fastapi import APIRouter, Request, Response, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Optional
from starlette.exceptions import HTTPException
from datetime import date
from app.users.service import UserService
from app.users.model import Users
from app.auth.service import create_token, hash_password
from datetime import date
