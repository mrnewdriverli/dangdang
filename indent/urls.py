from django.urls import path, include
from indent import views
app_name = 'indent'
urlpatterns = [
    path("indent/", views.indent, name="indent"),
    path("indent_ok/", views.indent_ok, name="indent_ok"),
    path("indent_logic/", views.indent_logic, name="indent_logic"),
    path("address/", views.address, name="address"),
    path("back_to_car/", views.back_to_car, name="back_to_car"),
]
#123