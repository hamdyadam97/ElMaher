from django.contrib import admin


# Register your models here.
from .models import User, Post, Comment, Service

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Service)




