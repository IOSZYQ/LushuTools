from django.shortcuts import render

# Create your views here.
import os, json
from toolset.viewUtils import viewResponse, viewErrorResponse
from rest_framework.views import APIView
from django.conf import settings

from Image.models import Image
from images import imageUtils, utils

class ImageView(APIView):
    def get(self, request, id):
        file_name = Image.objects.filter(id=id).values_list('file', flat=True).first()
        if file_name:
            file_name = os.path.join(settings.IMAGE_DIR, file_name)
            return viewResponse({"fileName": file_name})
        else:
            return viewErrorResponse("dont exist")

    def post(self, request):
        imgData = request.POST.get("imgData")

        if not imgData:
            imgData = json.loads(request.body.decode('utf-8'))["imgData"]

        fileName = utils.saveImageData(imgData)
        if fileName:
            image = Image.objects.create(imageName=fileName)
            return viewResponse({
                "id": image.id,
                "imageFile": fileName,
                "imageUrl": request.build_absolute_uri(imageUtils.imageUrl(fileName))
            })
        raise viewErrorResponse("Bad Upload")

    def delete(self, request, id):
        try:
            id = int(id)
        except:
            viewErrorResponse("id error")
        image = Image.objects.filter(id=id)
        if len(image) == 0:
            viewErrorResponse("image dont exist")
        else:
            #删除本地图片
            imageName = image.first().imageName
            for ext in ['.jpg', '.png']:
                filePath = settings.MEDIA_ROOT + '/images/' + imageName + ext
                if (os.path.exists(filePath)):
                    os.remove(filePath)
        image.delete()
        return viewResponse()


class ImageListView(APIView):
    def get(self, request):
        imageInfo = []
        for imageName in Image.objects.values('id', 'imageName').order_by('-id'):
            imageInfo.append({
                "id": imageName["id"],
                "imageFile": imageName["imageName"],
                "imageUrl": request.build_absolute_uri(imageUtils.imageUrl(imageName["imageName"]))
            })
        return viewResponse(imageInfo)