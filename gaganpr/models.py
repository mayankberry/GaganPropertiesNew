from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=12)
    desc = models.TextField()

    def __str__(self) :
        return self.name

class data(models.Model):
    dname = models.CharField(max_length=70)
    daddress = models.CharField(max_length=100)
    dphone = models.CharField(max_length=12)
    ddesc = models.TextField()

    def __str__(self) :
        return self.dname
