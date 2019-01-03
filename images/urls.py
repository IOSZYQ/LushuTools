__author__ = 'Swolfod'
# -*- coding: utf-8 -*-

from django.conf.urls import *
from images.views import *

urlpatterns = [
   url(r"^list/$", imageList, name="images.views.getList"),
   url(r"^delete/(\w+)/$", imageDelete, name="images.views.delete"),

   url(r"^status/$", getStatus, name="images.views.getImage"),
   url(r"^status/(\w+)/$", getStatus, name="images.views.getImage"),

   url(r"^getImage/(\w+)/$", getImage, name="images.views.getImage"),
   url(r"^getImage/(\w+)/(\d+)/$", getImage, name="images.views.getImage"),
   url(r"^getImage/(\w+)/(\d+)/(\d+)/$", getImage, name="images.views.getImage"),

   url(r"^staticImage/(\w+)/$", staticImage, name="images.views.staticImage"),
   url(r"^staticImage/(\w+)/(\d+)/$", staticImage, name="images.views.staticImage"),
   url(r"^staticImage/(\w+)/(\d+)/(\d+)/$", staticImage, name="images.views.staticImage"),
   url(r"^getFitImage/(\w+)/(\d+)/(\d+)/$", getFitImage, name="images.views.getFitImage"),
   url(r"^staticFitImage/(\w+)/(\d+)/(\d+)/$", staticFitImage, name="images.views.staticFitImage"),
   
   url(r"^load-url-data/$", loadImageFromUrl, name="images.views.loadImageFromUrl"),
   url(r"^load-url-data/(\d+)/$", loadImageFromUrl, name="images.views.loadImageFromUrl"),
   
   url(r"^loadStaticImageFromUrl/$", loadStaticImageFromUrl, name="images.views.loadStaticImageFromUrl"),
   url(r"^loadStaticImageFromUrl/(\d+)/$", loadStaticImageFromUrl, name="images.views.loadStaticImageFromUrl"),
   url(r"^uploadImageData/$", uploadImageData, name="images.views.uploadImageData"),
   url(r"^uploadImageData/(\d+)/$", uploadImageData, name="images.views.uploadImageData"),

   url(r"^upload-data/$", uploadImageData, name="images.views.uploadImageData"),
   url(r"^upload-data/(\d+)/$", uploadImageData, name="images.views.uploadImageData"),

   url(r"^uploadStaticImageData/$", uploadStaticImageData, name="images.views.uploadStaticImageData"),
   url(r"^uploadStaticImageData/(\w+)/$", uploadStaticImageData, name="images.views.uploadStaticImageData"),
   url(r"^uploadStaticImageData/(\w+)/(\d+)/$", uploadStaticImageData, name="images.views.uploadStaticImageData"),
   url(r"^editorUploadImg/$", editorUploadImg, name="images.views.editorUploadImg"),

]