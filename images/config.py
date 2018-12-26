__author__ = 'swolfod'

from django.conf import settings

IMAGE_ROOT = getattr(settings, 'MEDIA_ROOT', "./")

AccessKey = "DoocR93szuTVn0-S-_ujzIa9Qytpp_u7gpn5A97L"
SecretKey = "Q9vlkc_jBS_seov6Kfc250hTwM5ohMqatchOzNTn"

bucket_name = 'yinterest'
remote_domain = 'cdn-dev.lushu.com'

static_bucket_name = 'yinterest'
static_remote_domain = 'cdn-dev.lushu.com'