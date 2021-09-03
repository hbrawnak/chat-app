import os
from flask_pymongo import MongoClient


class Database:
    def __init__(self):
        self.host = os.getenv('DATABASE_HOST')
        self.driver = MongoClient("mongodb://" + self.host)

    def connect(self):
        try:
            return self.driver.chatapp
        except Exception as e:
            return "Database connection error"

    def get_db(self):
        return self.connect()
