from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient

def index(request):
    ingredients = Ingredient.objects.all().order_by('prepared_date')
    latest_ingredients = Ingredient.objects.order_by('-created_at')[:1]  # 4 รายการล่าสุด
    return render(request, 'main.html', {'ingredients': ingredients, 'latest_ingredients': latest_ingredients})

def delete_ingredient(request, ingredient_id):
    if request.method == "POST":
        ing = get_object_or_404(Ingredient, id=ingredient_id)
        ing.delete()
    return redirect('index')
