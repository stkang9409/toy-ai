import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key():
    return os.environ.get('OPENAI_API_KEY')


def get_db_connection_info():
    return {
        "host": os.environ.get('MYSQL_HOST'),
        "user": os.environ.get('MYSQL_USER'),
        "password": os.environ.get('MYSQL_PASSWORD'),
        "database": os.environ.get('MYSQL_DATABASE')
    }


def get_flask_secret_key():
    return os.environ.get('FLASK_SECRET_KEY')
