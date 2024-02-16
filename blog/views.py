from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Post,Comments
from .forms import CommentForm


#blog/list_all
class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html' 
    
#blog/detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_post.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = post
            myform.save()
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)

#blog/new
class CreatePost(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/blog/'
    template_name = 'blog/post_form.html'

#blog/pk/edit
class EditPost(UpdateView):
    model = Post
    fields = ['title', 'content', 'draft', 'tags', 'image']
    success_url = '/blog/'
    template_name = 'blog/edit.html'

#blog/delete
class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'