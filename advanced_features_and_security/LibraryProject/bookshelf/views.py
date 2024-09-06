from django.shortcuts import render


# bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your editing logic here
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Your creation logic here
    return render(request, 'create_book.html')



# bookshelf/views.py
from django.http import HttpResponseForbidden

def some_view(request):
    if not request.user.has_perm('bookshelf.can_view'):
        return HttpResponseForbidden()
    # Your view logic here
