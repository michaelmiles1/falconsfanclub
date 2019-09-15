from django.db import models

class Roster(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=4)
