from django.db import models
from django.conf import settings
from images.models import Image

from images.services import get_image_url_from_cloudflare
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def display_image_admin(self):
        if not self.image:
            return ""
        cloudflare_id = self.image.cloudflare_id
        return get_image_url_from_cloudflare(cloudflare_id, variant="admin")

