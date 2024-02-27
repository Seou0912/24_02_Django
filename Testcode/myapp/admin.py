# myapp/admin.py
from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")  # 목록에 표시할 필드
    search_fields = ["title", "author"]  # 검색 필드


admin.site.register(Book, BookAdmin)
