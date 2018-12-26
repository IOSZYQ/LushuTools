__author__ = 'swolfod'

import base64
import io
import os
import re
from io import BytesIO
from urllib.request import urlopen
from uuid import uuid1

from PIL import Image, ExifTags

from images import dataUtils, tasks
from images import imageService
from .config import *

DOMAIN_HOST = getattr(settings, 'DOMAIN_HOST', '')


def imageSize(imgSrc):
    try:
        match = re.search('[a-zA-Z0-9]{32}_([0-9]{0,5})x([0-9]{0,5})', imgSrc, re.IGNORECASE)
        return int(match.group(1)), int(match.group(2))
    except:
        return 0, 0


def saveImageData(base64Data, fileName=None, static=False, format="JPEG"):
    if "base64," in base64Data:
        base64Data = base64Data[base64Data.index("base64,") + 7:].strip()

    imgStr = io.BytesIO(base64.b64decode(base64Data))
    image = Image.open(imgStr)

    return saveImage(image, fileName=fileName, static=static, format=format)


def saveUploadedImage(uploaded, raw_data, static=False):
    """
    raw_data: if True, uploaded is an HttpRequest object with the file being
              the raw post data
              if False, uploaded has been submitted via the basic form
              submission and is a regular Django UploadedFile in request.FILES
    """
    try:
        # if the "advanced" upload, read directly from the HTTP request
        # with the Django 1.3 functionality
        if raw_data:
            foo = uploaded.read(1024)
            fileContent = foo
            while foo:
                foo = uploaded.read(1024)
                fileContent += foo
                # if not raw, it was a form upload so read in the normal Django chunks fashion

            image = Image.open(BytesIO(fileContent))
        else:
            fileContent = bytearray()
            for c in uploaded.chunks():
                fileContent += c
                # got through saving the upload, report success

            image = Image.open(BytesIO(fileContent))

        # if not RGB, convert
        if image.mode not in ("L", "RGB"):
            image = image.convert("RGB")

        return saveImage(image, static=False)
    except IOError as e:
        # could not open the file most likely
        pass
    return None


def saveImage(image, fileName=None, static=False, format="JPEG"):
    ext = "png" if format == "PNG" else "jpg"

    fileName = fileName.lower() if fileName else uuid1().hex
    if format != "JPEG":
        fileName += "_" + ext

    for orientationKey in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientationKey] == 'Orientation':
            break
    else:
        orientationKey = 0

    exif = image.info.get("exif", b"")
    if exif and orientationKey:
        try:
            if image._getexif():
                exifItems = dict(image._getexif().items())
                if exifItems[orientationKey] == 3:
                    image = image.rotate(180, expand=True)
                elif exifItems[orientationKey] == 6:
                    image = image.rotate(270, expand=True)
                elif exifItems[orientationKey] == 8:
                    image = image.rotate(90, expand=True)
        except:
            pass

    width, height = image.size
    fileName = '{0}_{1}x{2}.{3}'.format(fileName, width, height, ext)
    image.convert("RGB" if format == "JPEG" else "RGBA").save(
        os.path.join(IMAGE_ROOT, "images" if not static else "static", fileName).replace("\\", "/"), format,
        # exif=exif,
        quality=95, optimize=True, progressive=True)

    imageName = os.path.basename(fileName).split('.')[0]
    dataUtils.newLocalImage(imageName)

    # processThread = threading.Thread(target=imageService.remoteCacheImage,
    #                                  args=(imageName, bufferImageDone, None, static))
    # processThread.start()

    tasks.cloud_image_task.delay(image=imageName, static=static)

    return imageName


def imageFormat(imageName):
    return imageService.imageFormat(imageName)


def bufferImageDone(imageName):
    dataUtils.imageRemoted(imageName)


# def replaceImageWidth(contentStr, width):
#    return re.sub(r"(?<=/images/getImage/[a-zA-Z0-9]{32}_[0-9]+x[0-9]+/)[0-9]{1,4}(?=/)", str(width), contentStr)


def upperImageSize(imageName, width, height=None):
    m = re.match(r'^[a-zA-Z0-9]{32}_([0-9]+)x([0-9]+)$', imageName)
    if m:
        imgW = int(m.group(1))
        imgH = int(m.group(2))

        if height and width > imgW and height > imgH:
            return width, height

        if not height or imgW / imgH < width / height:
            height = int(imgH / imgW * width)
        else:
            width = int(imgW / imgH * height)

    return width, height


def loadImageFromUrl(externalUrl, fileName=None, static=False):
    if not externalUrl:
        return None

    if (DOMAIN_HOST and DOMAIN_HOST in externalUrl) or remote_domain in externalUrl:
        imageName = extractImageName(externalUrl)
        if imageName:
            return imageName

    fd = urlopen(externalUrl)
    imageContent = io.BytesIO(fd.read())
    image = Image.open(imageContent)
    fileName = saveImage(image, fileName, static)

    return fileName


def extractImageName(imageSrc):
    if not imageSrc or not imageSrc.strip():
        return None

    match = re.search(r'([a-zA-Z0-9]{32}_(?:png_)?[0-9]+x[0-9]+)', imageSrc)
    return match.group(1) if match else None
