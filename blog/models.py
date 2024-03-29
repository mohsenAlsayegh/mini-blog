from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager





class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 10000)
    author =models.ForeignKey(User, related_name = 'post_author', on_delete=models.CASCADE)
    draft = models.BooleanField(default = True)
    publish_date = models.DateTimeField(auto_now_add = True)
    tags = TaggableManager()
    image = models.ImageField(upload_to='blog',blank=True,null=True)

    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    post = models.ForeignKey(Post, related_name= 'comment_post',on_delete =models.CASCADE)
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE,null=True, blank=True)
    comment = models.TextField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.comment)