from django.urls import path
from .views import PostList,post_detail,CreatePost,EditPost,DeletePost
# from blog.api import PostListAPI


urlpatterns = [
    path('',PostList.as_view()),
    path('new',CreatePost.as_view()),
    path('<int:pk>/', post_detail),
    path('<int:pk>/edit', EditPost.as_view()),
    path('<int:pk>/delete', DeletePost.as_view()),
    
    
    #api urls
    
    #  path('blog/api', PostListAPI.as_view()),
    #  path('api/list', api.CommentAPI.as_view()),
     
]
