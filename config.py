import os
from os import environ

class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      CHANNEL = list(x for x in os.environ.get("CHANNEL_ID", "").replace("\n", " ").split(' '))
      DATABASE_URL = os.environ.get('DATABASE_URL', None)
      DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql") 
      SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "").split()]
