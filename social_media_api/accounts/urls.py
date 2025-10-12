from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserProfileAPIView, FollowUserAPIView, FollowingListAPIView,FollowersListAPIView, UnfollowUserAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/me/', UserProfileAPIView.as_view(), name='profile-me'),
    path('follow/<int:user_id>/', FollowUserAPIView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserAPIView.as_view(), name='unfollow-user'),
    path('followers/', FollowersListAPIView.as_view(), name='followers-list'),
    path('following/', FollowingListAPIView.as_view(), name='following-list'),
]