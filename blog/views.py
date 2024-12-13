from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # Optional: to paginate the list

# In your urls.py, you would add:
# from django.urls import path
# from .views import BlogListView
#
# urlpatterns = [
#     path('', BlogListView.as_view(), name='blog-list'),
# ]
