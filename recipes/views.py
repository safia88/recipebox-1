from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from recipes.models import Author, RecipeItems
from recipes.forms import AddRecipeForm, AddAuthorForm


# Create your views here.
def index(request):
    data = RecipeItems.objects.all()
    return render(request, 'index.html', {'data': data})

def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))    
    form = AddAuthorForm()
    return render(request, 'AddAuthorForm.html', {'form': form})


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItems.objects.create(
                title = data['title'],
                author = data['author'],
                description = data['description'],
                time = data['time'],
                instruction = data['instruction'],
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddRecipeForm()
    return render(request, 'AddRecipeForm.html', {'form': form})
    

def recipe_detail(request, pk):
    recipe = get_object_or_404(RecipeItems, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail(request, pk):
    author = get_object_or_404(RecipeItems, pk=pk)
    #post = RecipeItems.object.filter(author=person)
    return render(request, 'author_detail.html', {'recipe': author})