from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Sotuvchi(models.Model):
    name=models.CharField(max_length=50)
    mahsulot=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name