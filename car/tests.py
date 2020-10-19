import os, django

from django.test import TestCase

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dangdang.settings")
django.setup()
from user.models import User
from index.models import Book
from car.models import GoodsCar
# Create your tests here.
a = User.objects.filter(id=3)[0]
b = Book.objects.filter(id=4)[0]
GoodsCar.objects.create(user=a,book=b,num=2)

