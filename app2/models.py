from django.db import models

# Create your models here.

class Message(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.title
class Person(models.Model):
    name=models.CharField(max_length=50)
    p_mes=models.ForeignKey(Message,on_delete=models.CASCADE)
