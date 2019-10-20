from os import environ
import redis
SECRET_KEY = environ.get('SECRET_KEY')
FLASK_APP = environ.get('FLASK_APP')
FLASK_ENV=environ.get('FLASK_ENV')

SESSION_TYPE = environ.get('SESSION_TYPE')
SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))