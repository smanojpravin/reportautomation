from django.db import models
from django.db.models.base import Model

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    dateJoined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





