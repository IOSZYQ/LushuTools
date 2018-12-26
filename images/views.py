# Create your views here.

import json
import os

from django.contrib.auth.decorators import user_passes_test
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from sorl.thumbnail import get_thumbnail

from images import imageService, dataUtils, imageUtils, utils
from utilities.djangoUtils import respondJson, crossOrigin
from .config import *
from .utils import upperImageSize, imageFormat


def doGetImage(request, static, imageName, width=None, height=None, redirect=True):
    imageUrl = None

    if dataUtils.isLocal(imageName):
        folder = "static" if static else "images"

        formatInfo = imageFormat(imageName)
        ext = "." + formatInfo["ext"]

        contentType = formatInfo["contentType"]
        format = formatInfo["format"]

        filePath = os.path.join(IMAGE_ROOT, folder, imageName + ext).replace("\\", "/")
        imageFile = open(filePath, 'rb')

        if width:
            thumbSize = width
            if height is None:
                height = width

            if int(height) > 0:
                thumbSize = "{0}x{1}".format(thumbSize, height)

            im = get_thumbnail(imageFile, thumbSize, upscale=False, format=format)
            imageFile = open(os.path.join(IMAGE_ROOT, im.name).replace("\\", "/"), "rb")

        imageContent = imageFile.read()
        return HttpResponse(imageContent, content_type=contentType)

    if redirect:
        remoteUrl = imageService.remoteImageUrl(imageName, width, height, static=static)
        return HttpResponseRedirect(remoteUrl)

    return {
        'imageUrl': imageUrl,
        'ready': False
    }


def getStatus(request, imageName, width=None, height=None):
    return doGetImage(request, False, imageName, width, height, redirect=False)


def getImage(request, imageName, width=None, height=None):
    return doGetImage(request, False, imageName, width, height)


def staticImage(request, imageName, width=None, height=None):
    return doGetImage(request, True, imageName, width, height)


def getFitImage(request, imageName, width, height):
    width, height = upperImageSize(imageName, int(width), int(height))
    return doGetImage(request, False, imageName, str(width), str(height))


def staticFitImage(request, imageName, width, height):
    width, height = upperImageSize(imageName, int(width), int(height))
    return doGetImage(request, True, imageName, str(width), str(height))


def doLoadImageFromUrl(request, size, static=False):
    if request.method != "POST":
        return HttpResponseBadRequest()

    try:
        imageUrl = request.POST["imgSrc"]
        fileName = utils.loadImageFromUrl(imageUrl, static=static)

        if fileName:
            return respondJson({
                "imageFile": fileName,
                "imageUrl": request.build_absolute_uri(imageUtils.imageUrl(fileName, size, static=static))
            })

        raise Http404("Bad Upload")
    except Exception as e:
        return respondJson({"errMsg": str(e)}, False)


@csrf_exempt
@crossOrigin
def loadImageFromUrl(request, size=1000):
    return doLoadImageFromUrl(request, size)


@user_passes_test(lambda u: u.is_staff)
def loadStaticImageFromUrl(request, size=1000):
    return doLoadImageFromUrl(request, size, True)


def doUploadImageData(request, size, fileName=None, static=False):
    if request.method != "POST":
        return HttpResponseBadRequest()

    imgData = request.POST.get("imgData")

    if not imgData:
        imgData = json.loads(request.body.decode('utf-8'))["imgData"]

    fileName = utils.saveImageData(imgData, static=static)

    if fileName:
        return respondJson({
            "imageFile": fileName,
            "imageUrl": request.build_absolute_uri(imageUtils.imageUrl(fileName, size, static=static))
        })

    raise Http404("Bad Upload")


@csrf_exempt
def uploadImageData(request, size=None):
    return doUploadImageData(request, size)


@user_passes_test(lambda u: u.is_staff)
def uploadStaticImageData(request, fileName=None, size=1000):
    try:
        if fileName and int(fileName) == 0:
            fileName = None
    except:
        pass

    return doUploadImageData(request, size, fileName=fileName, static=True)


@csrf_exempt
def editorUploadImg(request):
    if request.method == "POST":
        if len(request.FILES) == 1:
            filename = utils.saveUploadedImage(list(request.FILES.values())[0], False)

            # save the file
            if filename:
                fileName = os.path.basename(filename).split('.')[0]

                return HttpResponse(json.dumps({
                    "files": [{
                        "url": request.build_absolute_uri(imageUtils.imageUrl(fileName))
                    }]
                }))

    raise Http404("Bad Upload")
