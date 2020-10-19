from django.urls import path, include
from index import views
app_name = 'index'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('booklist/', views.booklist, name='booklist'),
    path('bookdetails/', views.bookdetails, name='bookdetails'),

]