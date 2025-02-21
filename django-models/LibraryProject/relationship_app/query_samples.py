import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library (✅ Matches required format)
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)  # ⬅️ Fix: Use `.get()` instead of `library.librarian`

# Example Queries
if __name__ == "__main__":
    # Ensure data exists for testing
    author = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter 1", author=author)
    book2 = Book.objects.create(title="Harry Potter 2", author=author)

    library = Library.objects.create(name="City Library")
    library.books.set([book1, book2])

    librarian = Librarian.objects.create(name="John Doe", library=library)

    # Run sample queries
    print("Books by J.K. Rowling:", get_books_by_author("J.K. Rowling"))
    print("Books in City Library:", get_books_in_library("City Library"))
    print("Librarian of City Library:", get_librarian_for_library("City Library"))  # ✅ Should now pass the check
