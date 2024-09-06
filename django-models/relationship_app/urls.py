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

# project's urls.py (e.g., myproject/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('relationship_app.urls')),  # Include authentication URLs
]
