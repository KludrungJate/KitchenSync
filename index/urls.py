from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:ingredient_id>/', views.delete_ingredient, name='delete_ingredient'),
    path('add/', views.add_ingredient, name='add_ingredient'),  # เพิ่มบรรทัดนี้
]
