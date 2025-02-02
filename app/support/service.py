from database import get_connection
from app.support.model import Support


class SupportService:

    @staticmethod
    def save(support: Support):
        with get_connection() as conn:
            conn.cursor().execute('''INSERT INTO supporting (user_id, content) VALUES (%s, %s)''',
                                  (support.user_id, support.content))
