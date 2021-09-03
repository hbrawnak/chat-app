from datetime import datetime
from database.db import Database

db = Database().get_db()


class Message:
    """ Message Model """

    def __init__(self, text=None, user=None):
        self.text = text
        self.user = user
        self.create_at = datetime.now()

    def save_one(self):
        return db.messages.insert_one({"text": self.text, "created_at": self.create_at, "user": self.user})

    @classmethod
    def update_one(cls, where_key_value, set_key_value):
        return db.messages.update_one(where_key_value, {"$set": set_key_value})

    @classmethod
    def find_one(cls, where_key_value):
        return db.messages.find_one(where_key_value)

    @classmethod
    def find_all(cls, where_key_value=None, sort_desc=None, sort_asc=None, limit=None):
        query = db.messages
        query = query.find(where_key_value) if where_key_value else query.find()

        if sort_desc:
            query = query.sort(sort_desc, 1)
        if sort_asc:
            query = query.sort(sort_asc, -1)
        if limit:
            query = query.limit(limit)

        return query
