__author__ = "swolfod"

import os

DB_HOST = "127.0.0.1"
DB_PORT = ""
DB_NAME = "lushutools"
DB_USER = "root"
DB_PASSWORD = "1q2w3e4r"

QINIU_ACCESS_KEY = "DoocR93szuTVn0-S-_ujzIa9Qytpp_u7gpn5A97L"
QINIU_SECRET_KEY = "Q9vlkc_jBS_seov6Kfc250hTwM5ohMqatchOzNTn"

QINIU_IMAGE_BUCKET = 'yinterest'
QINIU_IMAGE_DOMAIN = 'cdn-dev.lushu.com'

QINIU_FILE_BUCKET = 'yinterest'
QINIU_FILE_DOMAIN = 'cdn-dev.lushu.com'

QINIU_STATIC_BUCKET = 'yinterest'
QINIU_STATIC_DOMAIN = 'cdn-dev.lushu.com'

PINGXX_API_KEY = "sk_test_irP8mHybjjH0m9y180rjvrrT"
PINGXX_PRIVATE_KEY_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tmp', 'pingxx_private_key.pem').replace('\\','/'))
PINGXX_APP_ID = "app_ezf1CCyDyXX1LKuf"

SMS_API_KEY = "4a3617d5e06e5b86f943efb0ad7b0ca3"

KF5_API_KEY = "6cf9c97f6725fb044089b3cac169c0"

DJANGO_SECRET_KEY = 'yo=fo_8%rdda+lorxn6p=*6(0=3f5()!ilwo5o@1#d5frplhly'

EMAIL_HOST = "smtp.163.com"
EMAIL_HOST_USER = "lushutest@163.com"
EMAIL_HOST_PASSWORD = "LushuTest123"

TEMPLATE_API_HOST = "127.0.0.1:8000/template/"
SEND_EMAIL_HOST = "http://127.0.0.1:8001/auth/send-email/"

ADMIN_TOKEN = '1q2w3e4r'
API_AUTH_TOKEN = 'API_DEVELOP'

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379

PASSWORD = "Lushu123"