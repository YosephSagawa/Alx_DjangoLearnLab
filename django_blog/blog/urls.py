from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'blog'


urlpatterns = [
    # Registration and profile
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),


    # Login / Logout using built-in views; templates expected in blog/ directory
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]