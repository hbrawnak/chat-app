import logging
import os
from flask_pymongo import MongoClient
import redis


class Database:
    """ Pooling DB Connection  """

    def __init__(self):
        self.host = os.getenv('DATABASE_HOST')

    def connect(self):
        try:
            client = MongoClient(self.host)
            return client.chatapp
        except Exception as e:
            logging.error('Database connection error')
            return 'Database connection error'

    def get_db(self):
        return self.connect()


class RedisDB:
    """ Pooling Redis Connection """

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
