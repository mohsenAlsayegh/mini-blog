from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html' 
    
    
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' 
    


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'content', 'draft', 'tags', 'image']
    template_name = 'blog/post_form.html'
    success_url = '/post_list/'
