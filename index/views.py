
from django.shortcuts import render
from .models import Ingredient

def index(request):
    ingredients = Ingredient.objects.all().order_by('prepared_date')
    latest_ingredients = Ingredient.objects.order_by('-created_at')[:4]  # 4 รายการล่าสุด
    return render(request, 'main.html', {'ingredients': ingredients, 'latest_ingredients': latest_ingredients})
