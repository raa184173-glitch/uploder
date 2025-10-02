#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21155770"))
API_HASH = environ.get("API_HASH", "f99c66d0ed9596517ce40bda8ad860d2")
BOT_TOKEN = environ.get("BOT_TOKEN", "7540047573:AAGD7L0V2GCUpqKAhPZEBh3CB6fU8PRYu1g")

OWNER = int(environ.get("OWNER", "7614763477"))
CREDIT = environ.get("CREDIT", "RRR")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7614763477').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))


