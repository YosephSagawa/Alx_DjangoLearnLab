from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserProfileAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/me/', UserProfileAPIView.as_view(), name='profile-me'),
]