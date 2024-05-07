from django.db import models

# Create your models here.
class Xabar(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.title
class Odam(models.Model):
    ism=models.CharField(max_length=50)
    tartib=models.ForeignKey(Xabar,on_delete=models.CASCADE)
