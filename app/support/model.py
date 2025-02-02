import json


class Support:

    def __init__(self, user_id: int, content: json, supporting_id: int = None):
        self.user_id = user_id
        self.content = content
        if supporting_id:
            self.supporting_id = supporting_id
