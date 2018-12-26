__author__ = 'swolfod'

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

def remoteFailed(info):
    print(info)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pieceful_Server.settings")

    import django
    django.setup()

    from images.models import LocalImage
    from images.dataUtils import imageRemoted
    from images.imageService import remoteCacheImage
    from images.utils import imageFormat
    from django.conf import settings

    localImages = LocalImage.objects.all()
    cnt = 0
    for localImage in localImages:
        try:
            ext = "." + imageFormat(localImage.imageName)["ext"]
            imageFilePath = os.path.join(settings.MEDIA_ROOT, "images", localImage.imageName + ext).replace("\\", "/")
            static = False

            if not os.path.exists(imageFilePath):
                imageFilePath = os.path.join(settings.MEDIA_ROOT, "static", localImage.imageName + ext).replace("\\", "/")
                static = True

            if not os.path.exists(imageFilePath):
                localImage.delete()
                continue

            remoteCacheImage(localImage.imageName, imageRemoted, remoteFailed, static)
        except Exception as e:
            continue

        cnt += 1
        if cnt % 100 == 0:
            print(cnt)