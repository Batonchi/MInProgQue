from database import get_connection
from app.articles.model import *


class PageService:

    @staticmethod
    def save(page: Page):
        with get_connection() as conn:
            conn.cursor().execute('''
                INSERT INTO articles (title, author, description, url, published_at, content) 
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
            result = cur.execute('''SELECT * FROM articles WHERE page_id = %S''', (article_id,))
            row = result.fetchone()
            if row:
                return Page(row[1], row[2], row[3], row[4], row[5], row[0])


class TextService:

    @staticmethod
    def save(text: Text):
        pass

    @staticmethod
    def get_text_by_id(text_id: int):
        pass

    @staticmethod
    def update_text_by_id(text_id: int, text: str):
        pass

    @staticmethod
    def drop_text_by_id(text_id: int):
        pass


class ImageService:

    @staticmethod
    def save(image: Image):
        pass

    @staticmethod
    def get_image_by_id(image_id: int):
        pass

    @staticmethod
    def drop_image_by_id(image_id: int):
        pass


class FeedBackService:

    @staticmethod
    def save(feedback: Feedback):
        pass


class LiterarySourcesService:

    @staticmethod
    def save(literary_sources: LiterarySources):
        pass



