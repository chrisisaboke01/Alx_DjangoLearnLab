from django.shortcuts import render
from django.views.generic import DetailView  # ✅ Ensure DetailView is used
from .models import Book, Library  # ✅ Ensure Library is imported

# Function-Based View (FBV) for listing books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View (CBV) for displaying library details
class LibraryDetailView(DetailView):
    model = Library  # ✅ Ensures CBV works correctly
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
