from flask_pymongo import MongoClient


def db_connection():
    """ MongoDb Connection """
    try:
        print('db connecting ...')
        # client = MongoClient("mongodb://127.0.0.1:27017/")
        client = MongoClient("mongodb://gateway.docker.internal:27017/")
        if client:
            print('success')
        return client.chatapp
    except Exception as e:
        print(str(e))
