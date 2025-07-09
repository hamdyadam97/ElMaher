from django.db import models
from django.db.models import Q
from django.utils.text import slugify

from section.models import Service
from user.models import User
from django.utils.translation import get_language,  gettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to=Q(is_staff=True) | Q(is_superuser=True))
    title_ar = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,unique=True)
    content_ar = models.TextField()
    content_en = models.TextField()
    image = models.ImageField(upload_to='post', verbose_name=_("Post Image"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="اختر خدمة مرتبطة بالمقال، أو اتركه فارغ ليكون المقال عام"
    )

    @property
    def title(self):

        return self.title_ar if get_language() == 'ar' else self.title_en

    @property
    def content(self):
        return self.content_ar if get_language() == 'ar' else self.content_en

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title_en, allow_unicode=True)
            slug = base_slug
            count = 1
            while Service.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = _("المدونة")
        verbose_name_plural = _("المدونة")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies',null=True,blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=255,unique=True)

    def save(self, *args, **kwargs):
        base_slug = slugify(self.post.title_en, allow_unicode=True)
        slug = base_slug
        count = 1
        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{count}"
            count += 1
        self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("التعليقات")
        verbose_name_plural = _("التعليقات")






#
# REASON_CHOICES = (
#     ('packing', 'تغليف ممتاز'),
#     ('delivery', 'توصيل سريع'),
#     ('price', 'أسعار مناسبة'),
#     ('support', 'خدمة عملاء ممتازة'),
#     ('other', 'أخرى'),
# )
# class Review(models.Model):
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
#     anonymous = models.BooleanField(default=False, help_text="اختر إذا كنت لا تريد عرض اسمك")
#     reason = models.CharField(max_length=20, choices=REASON_CHOICES)
#     title = models.CharField(max_length=255, verbose_name="عنوان التقييم")
#     content = models.TextField(verbose_name="محتوى التقييم")
#     rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
#     image = models.ImageField(upload_to='reviewers/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-created_at']
#
#     def display_name(self):
#         if self.anonymous or not self.user:
#             return "مستخدم مجهول"
#         return self.user.username
#
#     def __str__(self):
#         return f"{self.title} - {self.rating}/5"
#
