# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login  # Ensure this line is present exactly as shown
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)  # Using the login function here
            return redirect('home')  # Redirect to a home page or any desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'



# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if user is an admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if user is a member
def is_member(user):
    return user.userprofile.role == 'Member'

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



# relationship_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # Assuming you have a form for Book

# Add a new book (only users with 'can_add_book' permission)
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a list of books or another appropriate view
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# Edit an existing book (only users with 'can_change_book' permission)
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# Delete a book (only users with 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

