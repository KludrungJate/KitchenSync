from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:ingredient_id>/', views.delete_ingredient, name='delete_ingredient'),
]
