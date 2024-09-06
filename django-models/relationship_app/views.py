# relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView  # Ensure this import is included
from .models import Library  # Ensure this line is present exactly as shown
from .models import Book  # You can also import Book separately if needed

def list_books(request):
    # Query all books from the database
    books = Book.objects.all()
    # Render the list_books.html template with the list of books
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        # Override get_queryset to provide all libraries
        return Library.objects.all()
