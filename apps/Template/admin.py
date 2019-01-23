from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(TemplateFile)
admin.site.register(SendEmailInfo)