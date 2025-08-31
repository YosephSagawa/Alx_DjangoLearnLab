# Delete Operation

```python
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check if any books remain
Book.objects.all()
```

# Expected Output

(1, {'bookshelf.Book': 1})
<QuerySet []>
