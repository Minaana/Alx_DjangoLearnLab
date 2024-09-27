from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', views.profile_view, name='profile'),  # To be created in Step 4
]

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
