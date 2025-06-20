from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.text import slugify


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


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/',null=True,blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name, allow_unicode=True)
            slug = base_slug
            count = 1
            while Service.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name


# بوستات يكتبها staff/admin
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               limit_choices_to={'role__in': ['staff', 'admin']})
    title_ar = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    content_ar = models.TextField()
    content_en = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="اختر خدمة مرتبطة بالمقال، أو اتركه فارغ ليكون المقال عام"
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title_en

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



