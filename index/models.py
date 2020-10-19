from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    publisher = models.CharField(max_length=20, blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    words = models.BigIntegerField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    paper_size = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    current_price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    classify = models.ForeignKey('Classify', models.DO_NOTHING, db_column='classify', blank=True, null=True)
    introduct = models.CharField(max_length=1000, blank=True, null=True)
    comment_num = models.IntegerField(blank=True, null=True)
    sale_num = models.IntegerField(blank=True, null=True)
    pics = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'book'


class Classify(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    sup_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classify'
