from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  # Ensure both models are imported

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library  # Uses Django's DetailView for class-based structure
    template_name = "relationship_app/library_detail.html"  # Ensure template path is correct
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()  # Fetch related books
        return context
