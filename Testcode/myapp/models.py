from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)  # name
    description = models.TextField  # long description
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} / ({self.age}살)"
