from dotenv import load_dotenv
import os


# load .env
load_dotenv()


def get_openai_api_key():
    return os.environ.get('OPEN_AI_API_KEY')


def get_db_connection_info():
    return {
        host: os.environ.get('MYSQL_HOST'),
        user: os.environ.get('MYSQL_USER'),
        password: os.environ.get('MYSQL_PASSWORD'),
        database: os.environ.get('MYSQL_DATABASE')
    }
