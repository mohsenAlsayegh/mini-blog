from django.urls import path
from .views import PostList, post_detail, CreatePost, EditPost, DeletePost
from .api import PostListAPI, PostDetailAPI, CommentCreateAPI

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('new/', CreatePost.as_view(), name='create-post'),
    path('<int:pk>/', post_detail, name='post-detail'),
    path('<int:pk>/edit/', EditPost.as_view(), name='edit-post'),
    path('<int:pk>/delete/', DeletePost.as_view(), name='delete-post'),
    
    # API urls
    path('api/', PostListAPI.as_view(), name='api-post-list'),
    path('api/<int:pk>/', PostDetailAPI.as_view(), name='api-post-detail'),
    path('api/<int:pk>/comments/', CommentCreateAPI.as_view(), name='api-comment-create'),
]
