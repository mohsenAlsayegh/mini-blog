from django.urls import path
from .views import PostList,post_detail,CreatePost,EditPost,DeletePost


urlpatterns = [
    path('',PostList.as_view()),
    path('new',CreatePost.as_view()),
    path('<int:pk>/', post_detail),
    path('<int:pk>/edit', EditPost.as_view()),
    path('<int:pk>/delete', DeletePost.as_view()),
]
