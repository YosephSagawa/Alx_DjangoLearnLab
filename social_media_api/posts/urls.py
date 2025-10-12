from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedAPIView
from django.urls import path


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'feed', FeedAPIView, basename='feed')

urlpatterns = [
    path('feed/', FeedAPIView.as_view(), name='feed'),
]
urlpatterns = router.urls