from django.urls import path
from .views import list_books, LibraryDetailView  # ✅ Ensure these are imported

urlpatterns = [
    path('books/', list_books, name='list_books'),  # ✅ Function-Based View
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅ Class-Based View
]
