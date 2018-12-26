__author__ = 'swolfod'

from django import template
from images.imageUtils import imageUrl

register = template.Library()

@register.simple_tag
def image_url(imageName, width, height=None):
    return imageUrl(imageName, width, height)
