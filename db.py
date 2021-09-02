from flask_pymongo import MongoClient


def db_connection():
    """ MongoDb Connection """
    client = MongoClient("mongodb://127.0.0.1:27017/")
    return client.chatapp
