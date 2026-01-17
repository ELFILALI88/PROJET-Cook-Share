
from django.urls import path
from . import views
from .views import recipe_edit, recipe_delete
urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:id>/edit/', recipe_edit, name='recipe_edit'),
path('recipe/<int:id>/delete/', recipe_delete, name='recipe_delete'),

]


