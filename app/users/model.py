import json


from datetime import date


class UserBase:

    def __init__(self, first_name: str, last_name: str, avatar: str):
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

class UserCreate(UserBase):

        def __init__(self, first_name: str, last_name: str, avatar: str, email: str, password: str, special_word: str):
            super().__init__(first_name, last_name, avatar)
            self.email = email
            self.password = password
            self.special_word = special_word

class UserRead(UserCreate):
    
    def __init__(self, first_name: str, last_name: str, avatar: str, email: str, password: str, special_word: str, user_id: int, is_admin: bool):
         super().__init__(first_name, last_name, avatar, email, password, special_word)
         self.user_id = user_id
         self.is_admin = is_admin






class Favorite:

    def __init__(self, user_id: int, page_id: int, content: json):
        self.user_id = user_id
        self.page_id = page_id
        self.content = content
