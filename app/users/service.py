from database import get_connection
from app.users.model import User


class UserService:

    @staticmethod
    def save(user: User):
        pass

    @staticmethod
    def get_user_by_email_and_password(email: str):
        pass
