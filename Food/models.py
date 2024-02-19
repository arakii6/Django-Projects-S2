# From typing import iterable
from django.db import models
from django.contrib.auth.models import User
from .utils import generate_slug

# Create your models here
class Recipe(models.Model):
    user = models.ForeignKey(User, related_name = 'user_recipe', on_delete = models.CASCADE, null = True, blank = True)
    username = models.CharField(max_length = 150, blank = True, null = True)
    recipe_name = models.CharField(max_length = 100)
    recipe_description = models.TextField()
    recipe_image = models.FileField(upload_to = 'recipe images')
    slug = models.SlugField(unique = True, null = True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.recipe_name
    
    class Meta:
        verbose_name_plural = 'Recipe'