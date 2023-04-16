import logging

import mysql.connector
from flask import g

from common.config.load_config import get_db_connection_info


def init_db():
    logging.info("init_db")
    db_info = get_db_connection_info()
    return mysql.connector.connect(
        host=db_info['host'],
        user=db_info['user'],
        password=db_info['password'],
        database=db_info['database']
    )


def get_conn():
    if 'db' not in g:
        g.db = init_db()
    return g.db
