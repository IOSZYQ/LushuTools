from celery import shared_task

from images.imageService import remoteCacheImage
from images.dataUtils import imageRemoted


@shared_task
def cloud_image_task(image, static=False):
    cached = remoteCacheImage(image, static=static)
    if cached:
        imageRemoted(image)