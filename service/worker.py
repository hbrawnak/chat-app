import logging

from database.db import RedisDB
from rq import Queue
from rq import Retry

from service.helper import save_message

r = RedisDB().get_db()
q = Queue(connection=r)


def message_to_save(msg, user):
    try:
        save_message(msg, user)
        logging.info(f'task done for:  {user}')
    except Exception as e:
        logging.error(str(e))


def queue_worker(msg, user):
    q.name = 'message_queue'
    job = q.enqueue(message_to_save, msg, user, retry=Retry(max=3))
    return f'queue received with id:  {job.id}'
