from django.contrib import admin
from django.utils.html import format_html

from images.services import get_image_url_from_cloudflare
# Register your models here.
from .forms import BlogPostForm
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    fields = [ 'author', 'title', 'content', 'image_file', 'display_image', 'timestamp', 'updated']
    readonly_fields = ['display_image', 'timestamp', 'updated']
    # model = BlogPost
    form = BlogPostForm

    def display_image(self, obj):
        if not obj.image:
            return "No image"
        cloudflare_id = obj.image.cloudflare_id
        img_url = get_image_url_from_cloudflare(cloudflare_id, variant='admin')
        img_html = f'<img src="{img_url}" width="320" />'
        return format_html(img_html)

    display_image.short_description = 'Current image'


# admin.site.register(BlogPost, BlogPostAdmin)