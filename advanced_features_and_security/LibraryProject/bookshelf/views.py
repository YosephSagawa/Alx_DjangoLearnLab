from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import ExampleForm

# View Book (requires 'can_view')
@permission_required('your_app_name.can_view', raise_exception=True)
def book_list(request):
    """List all books"""
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

def example_form_view(request):
    """Render and process ExampleForm"""
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # handle data (save, send, etc.)
            return render(request, "bookshelf/form_example.html", {"form": form, "success": True})
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})

# Create Book (requires 'can_create')
@permission_required('your_app_name.can_create', raise_exception=True)
def book_create(request):
    # logic for creating book
    return render(request, "books/book_form.html")

# Edit Book (requires 'can_edit')
@permission_required('your_app_name.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # logic for editing book
    return render(request, "books/book_form.html", {"book": book})

# Delete Book (requires 'can_delete')
@permission_required('your_app_name.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # logic for deleting book
    return render(request, "books/book_confirm_delete.html", {"book": book})
