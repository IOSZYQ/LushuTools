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
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from Template.views import TemplateView, TemplateListView, SendEmail


# router = DefaultRouter()
#配置template的url
# router.register(r'template', TemplateInfoViewSet)


# template_list = TemplateViewSet.as_view({
#     'get': 'list',
#     # 'post': 'create'
# })

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    # url(r'docs/$', include_docs_urls(title="路书工具")),
    url(r'^template/list/', TemplateListView.as_view(), name='template_list'),
    url(r'^template/(\d+)/$', TemplateView.as_view(), name='template_info'),
    url(r'^template/', TemplateView.as_view(), name='template_info'),

    url(r'^email/', SendEmail.as_view(), name='send_email'),

    url(r'^images/', include('images.urls')),
    url(r'^tools/', include('Tools.urls')),
    # url(r'template/$', template_list, name='Template')
    # url(r'^', include(router.urls)),

]
