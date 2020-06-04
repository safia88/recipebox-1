from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_author/', views.add_author, name='add_author'),
    path('favourite/<int:pk>', views.favourite, name='favourite'),
    path('favourite_recipes/<int:pk>/',
         views.favourite_recipes, name='favourite_recipes'),
    path('recipe/<int:pk>/update/', views.update_recipe, name='update_recipe'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logoutview, name='logoutview')
]