from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view: List all books
def list_books(request):
    """Display all books and their authors"""
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# Class-based view: Show library details
class LibraryDetailView(DetailView):
    """Display details for a specific library and its books"""
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"  # will be available in template as {{ library }}
