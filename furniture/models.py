from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission
class User(AbstractUser):
    ROLE_CHOICES = (
        ('member', 'Member'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser



# بوستات يكتبها staff/admin
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               limit_choices_to={'role__in': ['staff', 'admin']})
    title_ar = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    content_ar = models.TextField()
    content_en = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title_en

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
