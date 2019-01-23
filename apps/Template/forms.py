# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/29 5:08 PM'
from django import forms

from .models import TemplateFile


class UploadTemplateForm(forms.ModelForm):
    class Meta:
        model = TemplateFile
        fields = ['file']
