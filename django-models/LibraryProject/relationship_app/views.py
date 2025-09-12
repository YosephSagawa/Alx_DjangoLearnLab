from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Book
from .models import Library


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration_app/register.html"

# Function-based view: List all books
def list_books(request):
    """Display all books and their authors"""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: Show library details
class LibraryDetailView(DetailView):
    """Display details for a specific library and its books"""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"  # will be available in template as {{ library }}
