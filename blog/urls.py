from django.urls import path
from .views import PostDetail,PostList,CreatePost


urlpatterns = [
    path('blog/new',CreatePost.as_view()),
    path('',PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    
    
    
]
