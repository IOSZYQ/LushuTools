__author__ = 'swolfod'

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YinterestServer.settings")

    import django
    django.setup()

    from images.dataUtils import newLocalImage
    import re
    from django.conf import settings

    import os
    for file in os.listdir(os.path.join(settings.MEDIA_ROOT, "images").replace("\\", "/")):
        m = re.search(r'([a-zA-Z0-9]{32}_[0-9]+x[0-9]+)', file)
        if m:
            newLocalImage(m.group(1))