from django.db import models
import datetime 

class Book(models.Model):
    name = models.CharField(max_length=200)