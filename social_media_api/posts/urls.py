from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedAPIView


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'feed', FeedAPIView, basename='feed')


urlpatterns = router.urls