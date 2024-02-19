# urls.py
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.Users.as_view()),
    path("myinfo", views.MyInfo.as_view()),
    # Authentication
    path("getToken", obtain_auth_token),  # DTF token
    path("login", views.Login.as_view()),  # Django Session Login
    path("login/jwt", JWTLogin.as_view()),  # jwt login
    path("login/jwt/info", views.UserDetailView.as_view()),
]
