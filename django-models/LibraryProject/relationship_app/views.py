from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Book
from .models import Library

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofle.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

class register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

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
