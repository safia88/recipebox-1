from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from recipes.models import Author, RecipeItems, FavouriteRecipes
from recipes.forms import AddRecipeForm, AddAuthorForm, LoginForm, SignupForm, RecipeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    data = RecipeItems.objects.all()
    return render(request, 'index.html', {'data': data})

@staff_member_required
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))    
    form = AddAuthorForm()
    return render(request, 'AddAuthorForm.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['username'],
                data['password'],
            )
            login(request, user)
            Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=user
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'SignupForm.html', {'form': form})


@login_required()
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

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                
                return HttpResponseRedirect(
                    request.GET.get('next' , reverse('homepage'))
                )
            
    form = LoginForm()
    return render(request, 'LoginForm.html', {'form': form})

def logoutview(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return HttpResponseRedirect(reverse('homepage')) 


@login_required()
def update_recipe(request, pk):
    print('Id: ', pk)
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(RecipeItems, pk=pk)

    # pass the object as instance in form
    form = RecipeForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_recipe.html", context)


def favourite_recipes(request, pk):
    author = Author.objects.get(pk=pk)
    data = FavouriteRecipes.objects.filter(user=author.user)
    return render(request, 'favourite-recipe.html', {'data': data})


@login_required()
def favourite(request, pk):
    recipe = RecipeItems.objects.get(pk=pk)
    favRec = FavouriteRecipes.objects.filter(recipe=recipe, user=request.user)
    if not favRec:
        FavouriteRecipes.objects.create(
            recipe=recipe,
            user=request.user)
    return HttpResponseRedirect(reverse('homepage'))
