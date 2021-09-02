from . import db

db = db.db_connection()


def get_chat_room_active_users():
    """ TODO need cache for 5 minutes in redis """
    return db.users.find({"isActive": True})
