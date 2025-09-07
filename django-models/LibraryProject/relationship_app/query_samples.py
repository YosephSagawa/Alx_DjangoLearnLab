# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # 1. Query all books by a specific author
    try:
        author = Author.objects.get(name="J.K. Rowling")
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("Author not found.")

    # 2. List all books in a library
    try:
        library = Library.objects.get(name="library_name")
        books_in_library = library.books.all()  # because ManyToMany
        print(f"\nBooks in {library.name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("Library not found.")

    # 3. Retrieve the librarian for a library
    try:
        library = Library.objects.get(name="Central Library")
        librarian = library.librarian  # OneToOne relationship
        print(f"\nThe librarian of {library.name} is {librarian.name}.")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or Librarian not found.")


if __name__ == "__main__":
    run_queries()
