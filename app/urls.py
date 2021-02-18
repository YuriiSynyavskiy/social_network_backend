from django.urls import path
from .views import register_user, get_user
from django.urls import path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register/', register_user, name="register_user"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', get_user, name="get_user"),
]
