from django.db import models

# Create your models here.

from index.models import Book
from django.db import models

from user.models import User


class Addressee(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    post_code = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addressee'


class List(models.Model):
    code = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    store = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    adressee = models.ForeignKey(Addressee, models.DO_NOTHING, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'list'


class BookList(models.Model):
    num = models.IntegerField(blank=True, null=True)
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)
    list = models.ForeignKey(List, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_list'
