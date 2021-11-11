from django.db import models
from django.db.models.base import Model
from django.forms.fields import IntegerField

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    image = models.ImageField(null=False)
    document = models.FileField(null=False)
    