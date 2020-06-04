from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class RecipeItems(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.CharField(max_length=10)
    instruction = models.TextField()
    
    def __str__(self):
        return self.title


class FavouriteRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeItems, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe
