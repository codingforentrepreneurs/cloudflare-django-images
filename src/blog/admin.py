from django.contrib import admin

# Register your models here.
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'author', 'timestamp', 'updated']
    readonly_fields = ['timestamp', 'updated']
    model = BlogPost


# admin.site.register(BlogPost, BlogPostAdmin)