from django.db import models

# Create your models here.
class Spesial(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu/images')
    price= models.DecimalField(max_digits=10, decimal_places=2)

class Terbaru(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu/images')
    description = models.TextField()

class Menu(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu/images')
    price= models.DecimalField(max_digits=10, decimal_places=2)
