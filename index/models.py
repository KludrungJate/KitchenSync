from django.db import models
from datetime import date, timedelta

class IngredientImage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='ingredient_images/')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    # เชื่อมกับ IngredientImage โดยใช้ ForeignKey (ถ้าหนึ่งภาพใช้ได้กับหลายวัตถุดิบ)
    # ถ้าอยากให้ภาพหนึ่งต่อหนึ่ง ใช้ OneToOneField
    image = models.ForeignKey(
        IngredientImage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ingredients"
    )
    prepared_date = models.DateField(default=date.today)  # auto ใส่วันนี้
    shelf_life_days = models.PositiveIntegerField(default=7)  # อายุวัตถุดิบ

    @property
    def expiry_date(self):
        return self.prepared_date + timedelta(days=self.shelf_life_days)

    @property
    def days_remaining(self):
        return (self.expiry_date - date.today()).days

    @property
    def image_url(self):
        # ถ้ามีการเชื่อม image ใช้รูปนั้น
        if self.image:
            return self.image.image.url
        # ถ้าไม่มี ให้ลองหา IngredientImage ที่ชื่อเดียวกัน
        img = IngredientImage.objects.filter(name=self.name).first()
        if img:
            return img.image.url
        return '/static/images/default.png'  # รูป default
