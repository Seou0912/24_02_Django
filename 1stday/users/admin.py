from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)  # UsersAdmin에 등록할 Model 지정 (Decorator)
class UsersAdmin(admin.ModelAdmin):  # ModelAdmin을 상속
    # pass
    list_display = ["name", "description", "age", "gender"]
    list_filter = ["age", "gender"]
    search_fields = ["name"]
