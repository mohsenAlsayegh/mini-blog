from django.contrib import admin

from .models import Post,Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'draft', 'author']
    list_filter = ['publish_date']  # Assuming you want to filter by the publish_date

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['post', 'user','created_at']
    list_filter = ['created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)



