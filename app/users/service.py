from database import get_connection
from app.users.model import UserCreate, UserRead


class UserService:

    @staticmethod
    def save(user: UserCreate):
        with get_connection() as conn:
            cursor = conn.cursor()
            query = ('insert into users (first_name, last_name, avatar, email, password, special_word)'
                    'values (%s, %s, %s, %s, %s, %s)')
            values = (user.first_name, user.last_name, user.avatar, user.email, user.password, user.special_word)
            cursor.execute(query, values)
            conn.commit()


    @staticmethod
    def find_by_email_and_password(email: str, password: str):
        with get_connection() as conn:
            cursor = conn.cursor()
            query = 'select first_name, last_name, avatar, email, password, special_word, user_id from users where email=%s and password=%s'
            values = (email, password)
            cursor.execute(query, values)
            result = cursor.fetchone() or None
            if result:
                result = UserRead(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
            return result
