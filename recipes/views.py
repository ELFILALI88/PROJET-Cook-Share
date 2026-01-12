from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


from django.shortcuts import render, get_object_or_404

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
