import json


class Page:

    def __init__(self, title: str, author: int, description: str, url: str, published_at: str, content: json,
                 page_id: int = None):
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.published_at = published_at
        self.content = content
        if page_id:
            self.page_id = page_id


class Image:

    def __init__(self, url: str, image_id: int = None):
        self.url = url
        if image_id:
            self.image_id = image_id


class Text:

    def __init__(self, type_content: str, content: str, text_id: int = None):
        self.type_content = type_content
        self.content = content
        if text_id:
            self.text_id = text_id


class Feedback:
    def __init__(self, user_id: int, page_id: int, feedback_id: int = None):
        self.user_id = user_id
        self.page_id = page_id
        if feedback_id:
            self.feedback_id = feedback_id


class LiterarySources:
    def __init__(self, content: json, source_id: int = None):
        self.content = content
        if source_id:
            self.source_id = source_id


