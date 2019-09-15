from django.db import models

class Home(models.Model):
    welcome = models.CharField(max_length=300)
    homeImage = models.FilePathField(path="/img")
    description = models.TextField()
