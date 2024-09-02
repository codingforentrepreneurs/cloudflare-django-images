import requests
from django.conf import settings


def upload_image_to_cloudflare(image_file):
    url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CLOUDFLARE_ACCOUNT_ID}/images/v1"
    headers = {"Authorization": f"Bearer {settings.CLOUDFLARE_API_KEY}"}

    with image_file.open("rb") as file:
        files = {"file": (image_file.name, file)}
        response = requests.post(url, headers=headers, files=files)

    response.raise_for_status()
    return response.json()["result"]["id"]

ALLOWED_VARIANTS = ['public', 'admin', 'adminDemo']

def get_image_url_from_cloudflare(image_id, variant="public"):
    url = settings.CLOUDFLARE_IMAGES_DOMAIN
    account_hash = settings.CLOUDFLARE_ACCOUNT_HASH
    final_variant = 'public'
    if variant in ALLOWED_VARIANTS:
        final_variant = variant
    return f"https://{url}/{account_hash}/{image_id}/{final_variant}"