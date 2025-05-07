from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True) #Date added at creation
    updated = models.DateTimeField(auto_now=True) #Date updated whenever object is saved