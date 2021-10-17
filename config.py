import os

class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      CHANNEL = list(x for x in os.environ.get("CHANNEL_ID", "").replace("\n", " ").split(' '))
      DATABASE_URL = os.environ.get('DATABASE_URL', None)
      DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql") 
      try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
