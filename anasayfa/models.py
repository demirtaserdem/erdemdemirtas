from django.db import models
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 50,verbose_name = "Ad ")
    surname = models.CharField(max_length = 50,verbose_name = "Soyad ")
