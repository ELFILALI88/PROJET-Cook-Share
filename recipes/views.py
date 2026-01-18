from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


 # el filali
@login_required
def recipe_edit(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    # 🔐 Sécurité : seul l’auteur peut modifier
    if recipe.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        recipe.title = request.POST['title']
        recipe.ingredients = request.POST['ingredients']
        recipe.instructions = request.POST['instructions']
        recipe.save()

        messages.success(request, "Recette modifiée avec succès")
        return redirect('recipe_detail', id=recipe.id)

    return render(request, 'recipes/recipe_edit.html', {'recipe': recipe})
@login_required
def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    # 🔐 Sécurité
    if recipe.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, "Recette supprimée avec succès")
        return redirect('home')

    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})
