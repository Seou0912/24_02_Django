# models.py
from django.db import models
from common.models import CommonModel


class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(null=True)
    reviews = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title
