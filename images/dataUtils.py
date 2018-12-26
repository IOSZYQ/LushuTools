__author__ = 'swolfod'

from django.core import cache

from images.models import LocalImage

cacheClient = cache.caches["redis"]


def newLocalImage(imageName):
    localImage = LocalImage()
    localImage.imageName = imageName
    localImage.ready = False
    localImage.save()

    cacheClient.set("images-local-{}".format(imageName), True)


def isLocal(imageName):
    localImage = cacheClient.get("images-local-{}".format(imageName))

    if not localImage:
        return False

    return True


def imageRemoted(imageName):
    LocalImage.objects.filter(imageName=imageName).update(ready=True)
    cacheClient.delete("images-local-{}".format(imageName))
