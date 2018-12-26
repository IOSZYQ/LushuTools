# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/26 3:04 PM'


from django.conf.urls import url, include
from Tools import views

emailUrlPatterns = [
    url("send/", views.SendEmail.as_view(), name="Email.sendEmail")
]

templateUrlPatterns = [
    url("list", views.TemplateFind.as_view(), name="Template.List"),
    url("upload", views.TemplateInfo.as_view(), name="Template.Upload"),
    url("delete/(\w+)/", views.TemplateInfo.as_view(), name="Template.Delete")
]


imageUrlPatterns = [

]

urlpatterns = [
    url("emial/", include(emailUrlPatterns)),
    url("image/", include(imageUrlPatterns))
]