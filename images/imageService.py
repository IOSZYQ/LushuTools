__author__ = 'swolfod'

import os

import qiniu

from images.config import *

IMAGE_PRIVATE = getattr(settings, 'IMAGE_PRIVATE', False)


def imageFormat(imageName):
    if "_png_" in imageName:
        return {
            "format": "PNG",
            "ext": "png",
            "contentType": "image/png"
        }
    else:
        return {
            "format": "JPEG",
            "ext": "jpg",
            "contentType": "image/jpeg"
        }


def remoteCacheImage(imageName, successHandler=None, failHandler=None, static=False):
    q = qiniu.Auth(AccessKey, SecretKey)
    # imageName = 'images/' + imageName
    # key = imageName
    key = 'images/' + imageName

    formatInfo = imageFormat(imageName)

    token = q.upload_token(bucket_name if not static else static_bucket_name, key)
    imageFilePath = os.path.join(settings.MEDIA_ROOT, "images" if not static else "static",
                                 imageName + "." + formatInfo["ext"]).replace("\\", "/")
    ret, info = qiniu.put_file(token, key, imageFilePath, mime_type=formatInfo["contentType"], check_crc=True)

    if ret and ret.get('key', None) == key:
        if successHandler:
            successHandler(imageName)
        return True

    elif failHandler:
        failHandler(info)
    return False


def remoteImageUrl(imageName, width=None, height=None, minSize=False, static=False):
    q = qiniu.Auth(AccessKey, SecretKey)

    # key = imageName
    key = 'images/' + imageName
    base_url = 'https://%s/%s?imageView2/%d' % (
        remote_domain if not static else static_remote_domain, key, 1 if minSize else 2)

    if width:
        base_url += "/w/" + str(width)

    if height:
        base_url += "/h/" + str(height)

    base_url += "/interlace/1/q/95"

    return q.private_download_url(base_url, expires=3600) if IMAGE_PRIVATE else base_url


def deleteImage(imageName):
    key = 'images/' + imageName
    q = qiniu.Auth(AccessKey, SecretKey)
    ret, info = qiniu.BucketManager(q).delete(bucket_name, key)
    if ret and ret.get('key', None) == key:
        return True
    return False

def deleteImages(imageNames):
    imageNames = imageNames if isinstance(imageNames, list) else [imageNames]
    keys = ['images/' + imageName for imageName in imageNames]

    q = qiniu.Auth(AccessKey, SecretKey)
    bucket = qiniu.BucketManager(q)
    ops = qiniu.build_batch_delete(bucket_name, keys)
    ret, info = bucket.batch(ops)