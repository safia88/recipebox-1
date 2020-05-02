from django.shortcuts import render, get_object_or_404
from recipes.models import Author, RecipeItems

# Create your views here.
def index(request):
    data = RecipeItems.objects.all()
    return render(request, 'index.html', {'data': data})

def recipe_detail(request, pk):
    recipe = get_object_or_404(RecipeItems, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail(request, pk):
    author = get_object_or_404(RecipeItems, pk=pk)
    return render(request, 'author_detail.html', {'recipe': author})