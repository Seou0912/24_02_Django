from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    date = models.DateTimeField(auto_now_add=True)
    likes = models.TextField()

    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(null=True)
    reviews = models.PositiveIntegerField(null=True)
