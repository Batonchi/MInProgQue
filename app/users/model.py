import json


from datetime import date


class User:

    def __init__(self, is_admin: bool, is_active: bool, date_reg: date, first_name: str, last_name: str, email: str,
                 password: str, special_word: str, avatar: str, favorites: json = None, user_id: int = None):
        self.is_admin = is_admin
        self.is_active = is_active
        self.date_reg = date_reg
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.special_word = special_word
        self.avatar = avatar
        self.favorites = favorites
        if user_id:
            self.user_id = user_id


class Favorite:

    def __init__(self, user_id: int, page_id: int, content: json):
        self.user_id = user_id
        self.page_id = page_id
        self.content = content
