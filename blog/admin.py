from django.contrib import admin

from .models import Post,Comments
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ['title', 'draft', 'author']
    list_filter = ['publish_date']  # Assuming you want to filter by the publish_date
    summernote_fields = ('content',)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'comment', 'created_at']
    list_filter = ['created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)



