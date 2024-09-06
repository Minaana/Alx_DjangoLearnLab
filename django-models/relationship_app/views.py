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
