from database.db import Database

db = Database().get_db()


class User:
    """ User model """

    def __init__(self, username=None):
        self.username = username
        self.isActive = True

    def save_one(self, username):
        return db.users.insert_one({"username": username, "isActive": self.isActive})

    @classmethod
    def update_one(cls, where_key_value, set_key_value):
        return db.users.update_one(where_key_value, {"$set": set_key_value})

    @classmethod
    def find_one(cls, where_key_value):
        return db.users.find_one(where_key_value)

    @classmethod
    def find_all(cls, where_key_value=None, sort_desc=None, sort_asc=None, limit=None):
        query = db.users
        query = query.find(where_key_value) if where_key_value else query.find()

        if sort_desc:
            query = query.sort(sort_desc, 1)
        if sort_asc:
            query = query.sort(sort_asc, -1)
        if limit:
            query = query.limit(limit)

        return query
