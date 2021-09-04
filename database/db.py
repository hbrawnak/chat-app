import logging
import os
from flask_pymongo import MongoClient
import redis


class Database:
    def __init__(self):
        self.host = os.getenv('DATABASE_HOST', 'host.docker.internal:27017')
        self.driver = MongoClient('mongodb://' + self.host)

    def connect(self):
        try:
            return self.driver.chatapp
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
