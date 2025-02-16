import json

from datetime import date


class Support:

    def __init__(self, user_id: int, date_sending: date, content: json, supporting_id: int = None):
        self.user_id = user_id
        self.date_sending = date_sending
        self.content = content
        if supporting_id:
            self.supporting_id = supporting_id
