# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # age = models.PositiveIntegerField(default=10)
    is_business = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, default="C")


# users/models.py


# def __str__(self):
#     return self.name


def __str__(self):
    return self.username  # f-string 도 가능
