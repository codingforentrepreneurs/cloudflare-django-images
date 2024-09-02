from django import forms

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
        print(image_file)
        cloudflare_id = upload_image_to_cloudflare(image_file)
        print(cloudflare_id)
        image_url = get_image_url_from_cloudflare(cloudflare_id)
        print(image_url)
        if commit:
            instance.save()
        return instance