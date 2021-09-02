import os
from flask_pymongo import MongoClient


def db_connection():
    """ MongoDb Connection """
    try:
        print('db connecting ...')
        client = MongoClient("mongodb://" + os.getenv('DATABASE_HOST'))
        if client:
            print('success')
        return client.chatapp
    except Exception as e:
        print(str(e))
