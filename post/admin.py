from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'author', 'created_at', 'service')
    list_filter = ('created_at', 'service')
    search_fields = ('title_ar', 'title_en', 'content_ar', 'content_en')
    ordering = ('-created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at',)
    list_filter = ('created_at', 'post')
    search_fields = ('post', 'text')
    ordering = ('-created_at',)


