# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/29 4:29 PM'
from django import forms

from .models import Image


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['imageName']
