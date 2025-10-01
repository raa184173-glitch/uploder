#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26772158"))
API_HASH = environ.get("API_HASH", "1999b08ff3abea90a962177e19487181")
BOT_TOKEN = environ.get("BOT_TOKEN", "7578519146:AAGBcI7oDptuN--M8FIbkP_sipavDS-6sRo")

OWNER = int(environ.get("OWNER", "8324507172"))
CREDIT = environ.get("CREDIT", "AR")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8324507172').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

