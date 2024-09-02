from django import forms

from images.models import Image
from images.services import (
    upload_image_to_cloudflare,
    get_image_url_from_cloudflare)

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)
    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'content']

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            cloudflare_id = upload_image_to_cloudflare(image_file)
            image_obj, created = Image.objects.get_or_create(
                title=self.cleaned_data['title'],
                defaults={
                    "cloudflare_id": cloudflare_id
                }
            )
            instance.image = image_obj
            # image_url = get_image_url_from_cloudflare(cloudflare_id)
        if commit:
            instance.save()
        return instance