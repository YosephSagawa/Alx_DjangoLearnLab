from django.urls import path
from .views import list_books,LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name="registration_app/login.html"), name="login"),
    path('logout/',LogoutView.as_view(template_name="registration_app/logout.html"), name="logout"),
    path('register/', views.register.as_view(), name="register"),
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
]
