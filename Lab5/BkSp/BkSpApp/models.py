from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200)
    site = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=12)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
