# admin.py
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("pk", "username", "email", "is_business", "grade")
    list_display_links = ("username", "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Personal info"),
            {"fields": ("email", "grade", "is_business")},
        ),
    )
