# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2019/1/25 4:03 PM'

import qiniu

from .config import *
from celery import shared_task

@shared_task
def remoteCacheImage(imageName, localfile):
    q = qiniu.Auth(AccessKey, SecretKey)
    key = imageName
    token = q.upload_token(bucket_name, key)
    ret, info = qiniu.put_file(token, key, localfile)
    if ret['key'] != key or ret['hash'] != qiniu.etag(localfile):
        return None
    return key



def remoteImageUrl(imageName):
    q = qiniu.Auth(AccessKey, SecretKey)
    key = imageName
    base_url = 'https://{}/{}'.format(remote_domain, key)
    return q.private_download_url(base_url)