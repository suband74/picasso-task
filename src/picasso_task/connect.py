import psycopg2
import logging.config
import os
from dotenv import load_dotenv

from settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('main.connect')

load_dotenv()

DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER_DB')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

def create_connection():
    try:
        conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    except:
        logger.error("Unable to connect to the database")

    return conn
