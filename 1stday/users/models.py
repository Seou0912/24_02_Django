from django.db import models


class User(models.Model):  # Model을 상속받는다
    name = models.CharField(max_length=20)  # 짧은 문장
    description = models.TextField()  # 긴 텍스트 문장
    age = models.PositiveIntegerField(null=True)  # 양의 정수형 숫자
    gender = models.CharField(max_length=20)


# users/models.py


# def __str__(self):
#     return self.name


def __str__(self):
    return f"{self.name} / ({self.age}살)"  # f-string 도 가능
