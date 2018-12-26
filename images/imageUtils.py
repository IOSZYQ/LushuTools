__author__ = 'swolfod'

from django.conf import settings
from django.urls import reverse

from images import imageService, dataUtils, utils

FAKE_DATA = getattr(settings, 'FAKE_DATA', False)
DOMAIN_HOST = getattr(settings, 'DOMAIN_HOST', '')


# @todo


def imageUrl(imageName, width=None, height=None, static=False):
    if dataUtils.isLocal(imageName):
        url = reverse("images.views.getImage" if not static else "images.views.staticImage",
                      args=(imageName, width, height) if height else ((imageName, width) if width else (imageName,)))
    else:
        url = imageService.remoteImageUrl(imageName, width, height, False, static)

    if url[:4] != "http" and DOMAIN_HOST:
        protocol = "http" if "127.0.0.1" in DOMAIN_HOST else "https"
        url = "{0}://{1}{2}".format(protocol, DOMAIN_HOST, url)

    return url


def upperImageUrl(imageName, width, height=None, static=False):
    if dataUtils.isLocal(imageName):
        if not height:
            width, height = utils.upperImageSize(imageName, width, height)
        return reverse("images.views.getFitImage" if not static else "images.views.staticFitImage",
                       args=(imageName, width, height) if height else (imageName, width))
    else:
        return imageService.remoteImageUrl(imageName, width, height, True, static)


def patternImageUrl(imageFile, mode=1, width=None, height=None, static=False):
    def getFakeImageSize(imageFile):
        fakeW = 18739275174
        fakeH = 68492461732

        while str(fakeW) in imageFile:
            fakeW += 1

        while str(fakeH) in imageFile or fakeH == fakeW:
            fakeH += 1

        return fakeW, fakeH

    if not imageFile:
        if not FAKE_DATA:
            return None
        imageFile = "c29eacf4cfab11e4b5ee3c15c2ca2442_640x852"

    if imageFile and imageFile.startswith("http"):
        imageFile = utils.extractImageName(imageFile)

    fakeW, fakeH = getFakeImageSize(imageFile)
    urlFunc = upperImageUrl if mode != 2 else imageUrl

    if width:
        url = urlFunc(imageFile, width, height, static=static)
    else:
        url = urlFunc(imageFile, fakeW, fakeH, static=static).replace(str(fakeW), "{width}").replace(str(fakeH),
                                                                                                     "{height}")

    if url[:4] != "http" and DOMAIN_HOST:
        protocol = "http" if "127.0.0.1" in DOMAIN_HOST else "https"
        url = "{0}://{1}{2}".format(protocol, DOMAIN_HOST, url)

    return url
