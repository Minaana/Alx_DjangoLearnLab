# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL pattern for function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for class-based view
]

# relationship_app/urls.py
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]

# relationship_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Correct usage of LoginView with template_name
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Correct usage of LogoutView with template_name
    path('register/', views.register, name='register'),  # Directly linking to views.register
]


# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),
]