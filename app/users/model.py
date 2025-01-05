import json


class User:

    def __init__(self, is_admin: bool, first_name: str, last_name: str, email: str, password: str,
                 special_word: str, avatar: str, favorites: json, user_id: int = None):
        self.is_admin = is_admin
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.special_word = special_word
        self.avatar = avatar
        self.favorites = favorites
        if user_id:
            self.user_id = user_id

