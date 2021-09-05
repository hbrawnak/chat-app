import logging
import os
from flask_pymongo import MongoClient
import redis


class Database:
    def __init__(self):
        self.host = os.getenv('DATABASE_HOST')
        self.db_cred = os.getenv('DATABASE_CRED')

    def connect(self):
        try:
            client = MongoClient('mongodb+srv://' + self.db_cred + self.host + '?retryWrites=true&w=majority')
            return client.chatapp
        except Exception as e:
            logging.error('Database connection error')
            return 'Database connection error'

    def get_db(self):
        return self.connect()


class RedisDB:
    def __init__(self):
        self.host = os.getenv('REDIS_HOST', 'redis_server')

    def connect(self):
        try:
            return redis.Redis(host=self.host)
        except Exception as e:
            logging.error('Redis connection error')
            return 'Redis connection error'

    def get_db(self):
        return self.connect()
