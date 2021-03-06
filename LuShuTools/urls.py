"""LuShuTools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from Template.views import TemplateView, TemplateListView, SendEmail, ToolsView
from Image.views import ImageView, ImageListView


urlpatterns = [
    url(r'^$', ToolsView.as_view(), name='tool_list'),

    url(r'^template/list/', TemplateListView.as_view(), name='template_list'),
    url(r'^template/(\d+)/$', TemplateView.as_view(), name='template_info'),
    url(r'^template/', TemplateView.as_view(), name='template_info'),

    url(r'^image/list/', ImageListView.as_view(), name='upload_image'),
    url(r'^image/(\d+)/$', ImageView.as_view(), name='template_info'),
    url(r'^image/', ImageView.as_view(), name='upload_image'),

    url(r'^email/', SendEmail.as_view(), name='send_email'),

]
