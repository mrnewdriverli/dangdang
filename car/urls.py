from django.urls import path, include
from car import views
app_name = 'car'
urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("add_goods/", views.add_goods, name="add_goods"),
    path("delete_goods/", views.delete_goods, name="delete_goods")
]