from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    
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