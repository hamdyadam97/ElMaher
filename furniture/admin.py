from django.contrib import admin


# Register your models here.
from .models import User, Post, Comment, Service, Review

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Service)



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'user', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['title', 'content', 'name']
