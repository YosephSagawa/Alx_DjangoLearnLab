from django import forms
from .models import Book

class ExampleForm(forms.Form):
    """A simple example form for demonstration (used in form_example.html)."""
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)


# Optional: if you want to tie it to your Book model
class BookSearchForm(forms.Form):
    """Form for searching books by title (used in book_list view)."""
    title = forms.CharField(required=False, max_length=100)
