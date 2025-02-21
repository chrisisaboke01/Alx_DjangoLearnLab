from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # ✅ Add this if missing

# Function-Based View (FBV) for listing books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View (CBV) for displaying library details
class LibraryDetailView(DetailView):
    model = Library  # ✅ Required for CBV
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
