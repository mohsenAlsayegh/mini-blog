
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from . serializers import PostSerializer
from .models import Post



class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['comments']
    
#  class CommentAPI(generics.ModelViewSet):
#     pass



    