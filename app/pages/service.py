from database import get_connection
from app.pages.model import *


class PageService:

    @staticmethod
    def save(page: Page):
        with get_connection() as conn:
            conn.cursor().execute('''
                INSERT INTO pages (title, author, description, url, published_at, content) 
                VALUES (%s, %s, %s, %s, %s, %s)''',
                                  (page.title, page.author, page.description,
                                   page.url, page.published_at, page.content))
            conn.commit()

    @staticmethod
    def get_article_content_by_id(article_id: int):
        pass

    @staticmethod
    def get_article_by_id(article_id: int):
        with get_connection() as conn:
            cur = conn.cursor()
            result = cur.execute('''SELECT * FROM pages WHERE page_id = %S''', (article_id,))
            row = result.fetchone()
            if row:
                return Page(row[1], row[2], row[3], row[4], row[5], row[0])


class TextService:

    @staticmethod
    def save(text: Text):
        with get_connection() as conn:
            conn.cursor().execute('''
                INSERT INTO texts (type_content, content) VALUES (%s, %s)''', (text.type_content, text.content))
            conn.commit()

    @staticmethod
    def get_text_by_id(text_id: int):
        with get_connection() as conn:
            cur = conn.cursor()
            result = cur.execute('''SELECT * FROM texts WHERE text_id = %s''', (text_id, )).fetchone()
            if result:
                return Text(result.type_content, result.content, result.text_id)

    @staticmethod
    def drop_text_by_id(text_id: int):
        with get_connection() as conn:
            conn.cursor().execute('''DELETE FROM texts WHERE text_id = %s''', (text_id, ))
            conn.commit()


class ImageService:

    @staticmethod
    def save(image: Image):
        with get_connection() as conn:
            conn.cursor().execute('''INSERT INTO images (url) VALUES (%s)''', (image.url, ))
            conn.commit()

    @staticmethod
    def get_image_by_id(image_id: int):
        with get_connection() as conn:
            return conn.cursor().execute('''SELECT * FROM images WHERE image_id = %s''', (image_id, )).fetchone()

    @staticmethod
    def drop_image_by_id(image_id: int):
        with get_connection() as conn:
            conn.cursor().execute('''DELETE FROM images WHERE image_id = %s''', (image_id, ))
            conn.commit()


class FeedBackService:

    @staticmethod
    def save(feedback: Feedback):
        with get_connection() as conn:
            conn.cursor().execute('''INSERT INTO feedbacks (user_id, page_id, content) VALUES (%s, %s, %s)''',
                                  (feedback.user_id, feedback.page_id, feedback.content))
            conn.commit()


class LiterarySourcesService:

    @staticmethod
    def save(literary_sources: LiterarySources):
        with get_connection() as conn:
            conn.cursor().execute('''INSERT INTO literary_sources (content) VALUES (%s)''',
                                  (literary_sources.content, ))
            conn.commit()



