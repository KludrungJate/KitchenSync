from django.contrib import admin
from .models import Ingredient, IngredientImage
admin.site.register(Ingredient, list_display=['name', 'quantity', 'prepared_date', 'shelf_life_days', 'expiry_date', 'days_remaining'])
@admin.register(IngredientImage)
class IngredientImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" />'
        return 'ไม่มีรูป'
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'