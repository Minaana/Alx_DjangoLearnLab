from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def profile_view(request):
    if request.method == 'POST':
        # Handle profile update logic here
        pass
    return render(request, 'registration/profile.html')

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# List all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template to render the post list
    context_object_name = 'posts'
    ordering = ['-published_date']  # Order by the most recent

# Show individual blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Allow authenticated users to create new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to the logged-in user
        return super().form_valid(form)

# Allow post authors to update their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only author can update

# Allow post authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only author can delete
