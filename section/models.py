from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language,  gettext_lazy as _


class AboutUs(models.Model):
    why_us_ar = models.TextField(verbose_name="لماذا نحن (عربي)")
    why_us_en = models.TextField(verbose_name="Why Us (English)")

    history_ar = models.TextField(verbose_name="تاريخنا (عربي)")
    history_en = models.TextField(verbose_name="Our History (English)")

    services_ar = models.TextField(verbose_name="خدماتنا (عربي)")
    services_en = models.TextField(verbose_name="Our Services (English)")

    AboutUs_ar = models.TextField(verbose_name="عنا  (عربي)")
    AboutUs_en = models.TextField(verbose_name="ِAbout Us (English)")

    image = models.ImageField(upload_to='about_us', verbose_name=_("Company Image"))

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def history(self):
        return self.history_ar if get_language() == 'ar' else self.history_en

    @property
    def services(self):
        return self.services_ar if get_language() == 'ar' else self.services_en

    @property
    def why_us(self):
        return self.why_us_ar if get_language() == 'ar' else self.why_us_en

    @property
    def about_us(self):
        return self.AboutUs_ar if get_language() == 'ar' else self.AboutUs_en

    class Meta:
        verbose_name = "من نحن"
        verbose_name_plural = "محتوى من نحن"

    def __str__(self):
        return f"من نحن - {self.created_at.strftime('%Y-%m-%d')}"


class Service(models.Model):
    name_ar = models.TextField(verbose_name=" اسم الخدمة (عربي)")
    name_en = models.TextField(verbose_name="name service Us (English)")
    slug = models.CharField(max_length=255,unique=True)
    services_ar = models.TextField(verbose_name="وصف الخدمة (عربي)")
    services_en = models.TextField(verbose_name="description Service (English)")

    image = models.ImageField(upload_to='service', verbose_name=_("service Image"))

    created_at = models.DateTimeField(auto_now_add=True)
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
    @property
    def service(self):
        return self.services_ar if get_language() == 'ar' else self.services_en

    @property
    def name(self):
        return self.name_ar if get_language() == 'ar' else self.name_en

    class Meta:
        verbose_name = "خدمتنا"
        verbose_name_plural = "محتوى خدمتنا  "

    def __str__(self):
        return f"خدمتنا  - {self.created_at.strftime('%Y-%m-%d')}"


class Work(models.Model):
    name_ar = models.TextField(verbose_name=" اسم العمل (عربي)")
    name_en = models.TextField(verbose_name="name Work Us (English)")
    slug = models.CharField(max_length=255,unique=True)
    work_ar = models.TextField(verbose_name="وصف العمل (عربي)")
    work_en = models.TextField(verbose_name="description Works (English)")

    image = models.ImageField(upload_to='work/images', verbose_name=_("Work Image"),null=True, blank=True)

    video = models.FileField(upload_to='work/videos', verbose_name=_("Work Video"), blank=True, null=True)
    video_image = models.ImageField(upload_to='work/videos', verbose_name=_("Work Video Image"), blank=True, null=True)

    img_web = models.ImageField(upload_to='work/web_images', verbose_name=_("Web View Image"), blank=True, null=True)
    url_web = models.URLField(verbose_name=_("Website URL"), blank=True, null=True)

    CATEGORY_CHOICES = (
        (1, "Image"),
        (2, "Video"),
        (3, "Web URL"),
    )

    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

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
    def clean(self):
        media_fields = [self.image, self.video, self.img_web]
        filled_fields = [field for field in media_fields if field]

        if len(filled_fields) == 0:
            raise ValidationError(_("يجب إدخال صورة أو فيديو أو رابط نت واحد فقط."))

        if len(filled_fields) > 1:
            raise ValidationError(_("يُسمح فقط بإدخال واحد من: صورة، فيديو، أو رابط نت."))

        if self.img_web and not self.url_web:
            raise ValidationError(_("يرجى رفع صورة للموقع أو إدخال رابط الموقع."))
        if self.url_web and not self.img_web:
            raise ValidationError(_("يرجى رفع صورة للموقع أو إدخال رابط الموقع."))

        if self.video and not self.video_image:
            raise ValidationError(_("يرجى رفع صورة للموقع أو إدخال فيويدو الموقع."))
        if self.video_image and not self.video:
            raise ValidationError(_("يرجى رفع صورة للموقع أو إدخال فيويدو الموقع."))

        # تحديد التصنيف حسب الحقل الموجود
        if self.image:
            self.category = 1
        elif self.video:
            self.category = 2
        elif self.img_web:
            self.category = 3

    @property
    def work(self):
        return self.work_ar if get_language() == 'ar' else self.work_en

    @property
    def name(self):
        return self.name_ar if get_language() == 'ar' else self.name_en

    class Meta:
        verbose_name = "اعمالنا"
        verbose_name_plural = "محتوى اعمالنا"

    def __str__(self):
        return f"اعمالنا  - {self.created_at.strftime('%Y-%m-%d')}"

