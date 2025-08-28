from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient, IngredientImage
from datetime import date

def index(request):
    ingredients = Ingredient.objects.all().order_by('prepared_date')
    latest_ingredients = Ingredient.objects.order_by('-created_at')[:1]  # 4 รายการล่าสุด
    return render(request, 'main.html', {'ingredients': ingredients, 'latest_ingredients': latest_ingredients})

def delete_ingredient(request, ingredient_id):
    if request.method == "POST":
        ing = get_object_or_404(Ingredient, id=ingredient_id)
        ing.delete()
    return redirect('index')

def add_ingredient(request):
    today = date.today().isoformat()
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = int(request.POST.get("quantity", 1))
        prepared_date = request.POST.get("prepared_date")
        expiry_date = request.POST.get("expiry_date")
        shelf_life_days = (
            date.fromisoformat(expiry_date) - date.fromisoformat(prepared_date)
        ).days

        image_file = request.FILES.get("image_file")
        image_obj = None
        if image_file:
            # สร้าง IngredientImage ใหม่ทุกครั้ง
            image_obj = IngredientImage.objects.create(name=name, image=image_file)

        Ingredient.objects.create(
            name=name,
            quantity=quantity,
            prepared_date=prepared_date,
            shelf_life_days=shelf_life_days,
            image=image_obj
        )
        return redirect('index')
    return render(request, 'add.html', {'today': today})
