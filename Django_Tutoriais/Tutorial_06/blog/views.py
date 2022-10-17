from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
<<<<<<< HEAD
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
=======
    template_name = 'post_detail.html'
>>>>>>> 0f34069531d58b2ce86903428c8cef0c7024d676
