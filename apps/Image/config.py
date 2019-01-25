__author__ = 'swolfod'

from django.conf import settings
import secretKeys

IMAGE_ROOT = getattr(settings, 'MEDIA_ROOT', "./")

AccessKey = secretKeys.QINIU_ACCESS_KEY
SecretKey = secretKeys.QINIU_SECRET_KEY

bucket_name = secretKeys.QINIU_IMAGE_BUCKET
remote_domain = secretKeys.QINIU_IMAGE_DOMAIN

static_bucket_name = secretKeys.QINIU_STATIC_BUCKET
static_remote_domain = secretKeys.QINIU_STATIC_DOMAIN