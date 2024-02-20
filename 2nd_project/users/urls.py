from django.urls import path
from . import views

urlpatterns = [path("", views.Models.as_view())]
