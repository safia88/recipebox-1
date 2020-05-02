from django.contrib import admin
from recipes.models import Author, RecipeItems

# Register your models here.
admin.site.register(Author)
admin.site.register(RecipeItems)
