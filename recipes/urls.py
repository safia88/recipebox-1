from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail')
]