from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    pages = models.IntegerField()
    published = models.DateField()
    is_published = models.BooleanField(default=True)
