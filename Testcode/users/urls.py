from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
		TokenVerifyView, path
)

urlpatterns = [
		# simple JWT
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view())
]