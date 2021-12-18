from django.db import models

class Computer(models.Model):
    brand = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    
class Disk(models.Model):
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    def __str__(self):
        return self.size
