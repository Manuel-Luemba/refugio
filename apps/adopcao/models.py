from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    tel = models.CharField(max_length=12)
    email = models.EmailField()
    adress = models.TextField()

