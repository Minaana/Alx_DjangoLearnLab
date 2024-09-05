from django.shortcuts import render
from .models import Book

def list_books(request):
    # Query all books from the database
    books = Book.objects.all()
    # Render the list_books.html template with the list of books
    return render(request, 'relationship_app/list_books.html', {'books': books})



from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        # Override get_queryset to provide all libraries
        return Library.objects.all()
