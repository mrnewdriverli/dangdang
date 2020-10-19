from django.db import models

# Create your models here.
from index.models import Book
from user.models import User


class GoodsCar(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(Book, models.DO_NOTHING, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_car'
