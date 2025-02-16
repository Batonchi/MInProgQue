from base.database import get_connection
from app.users.schemas import UserCreate, UserRead
from app.users.model import User
from base.service import BaseService

class UserService(BaseService):
    model = User
