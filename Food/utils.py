from django.utils.text import slugify
import uuid

def generate_slug(title):
    from .models import Recipe
    title = slugify(title)

    while Recipe.objects.filter(slug = title).exists():
        title = f'{title}-{str(uuid.uuid4())[:4]}'

    return title

