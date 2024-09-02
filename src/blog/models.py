from django.db import models
from django.conf import settings
from images.models import Image

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

