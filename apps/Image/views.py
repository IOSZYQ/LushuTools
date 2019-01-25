from django.shortcuts import render

# Create your views here.
import os, json

from toolset.viewUtils import viewResponse, viewErrorResponse
from rest_framework.views import APIView
from Image.models import Image

from .tasks import *

class ImageView(APIView):
    def get(self, request, id):
        image = Image.objects.filter(id=id).values_list('file', flat=True).first()
        if image:
            return viewResponse({
                "id": image.id,
                "imageFile": image.imageName,
                "imageUrl": request.build_absolute_uri(remoteImageUrl(image.imageName))
            })
        else:
            return viewErrorResponse("dont exist")

    def post(self, request):
        imagePath = request.POST.get("path")
        imageName = request.POST.get("name")
        imageName = imageName.replace(' ', '').replace('/', '_')
        if len(Image.objects.filter(imageName=imageName)):
            return viewErrorResponse("照片已经存在")
        key = remoteCacheImage.delay(imageName, localfile=imagePath)
        if key:
            image = Image.objects.create(imageName=imageName)
            return viewResponse({
                "id": image.id,
                "imageFile": image.imageName,
                "imageUrl": request.build_absolute_uri(remoteImageUrl(image.imageName))
            })
        return viewErrorResponse("Bad Upload")

    def delete(self, request, id):
        try:
            id = int(id)
        except:
            viewErrorResponse("id error")
        Image.objects.filter(id=id).delete()
        return viewResponse()


class ImageListView(APIView):
    def get(self, request):
        imageInfo = []
        for imageName in Image.objects.values('id', 'imageName').order_by('-id'):
            imageInfo.append({
                "id": imageName["id"],
                "imageFile": imageName["imageName"],
                "imageUrl": request.build_absolute_uri(remoteImageUrl(imageName["imageName"]))
            })
        return viewResponse(imageInfo)


