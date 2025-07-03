from django.utils.translation import gettext_lazy as _, get_language
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text=_('The groups this user belongs to.'),
        verbose_name=_('groups')
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions')
    )

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    def __str__(self):
        return self.username


class JobTitles(models.TextChoices):
    MANAGER = "manager", _("Manager")
    ACCOUNTANT = "accountant", _("Accountant")
    DRIVER = "driver", _("Driver")
    PACKER = "packer", _("Packager")
    TECHNICIAN = "technician", _("Technician")
    CRAFTSMAN = "craftsman", _("Craftsman")


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("User"))
    full_name_ar = models.CharField(_("Full Name Arabic"), max_length=100)
    full_name_en = models.CharField(_("Full Name English "), max_length=100)
    job_title = models.CharField(_("Job Title"), max_length=50, choices=JobTitles.choices)
    description_ar = models.TextField(_("الوصف بالعربية"), blank=True, null=True)
    description_en = models.TextField(_("Description in English"), blank=True, null=True)
    phone_number = models.CharField(_("Phone Number"), max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(_("Profile Picture"), upload_to='employees/', blank=True, null=True)
    birth_date = models.DateField(_("Birth Date"), blank=True, null=True)
    address = models.TextField(_("Address"), blank=True, null=True)
    linkedin = models.URLField(_("LinkedIn"), blank=True, null=True)
    facebook = models.URLField(_("Facebook"), blank=True, null=True)
    twitter = models.URLField(_("Twitter"), blank=True, null=True)
    instagram = models.URLField(_("Instagram"), blank=True, null=True)
    google = models.URLField(_("Google"), blank=True, null=True)

    is_active = models.BooleanField(_("Is Active"), default=True)
    date_joined = models.DateField(_("Date Joined"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    @property
    def description(self):
        return self.description_ar if get_language() == 'ar' else self.description_en

    @property
    def full_name(self):
        return self.full_name_ar if get_language() == 'ar' else self.full_name_en

    def clean(self):
        # إذا الوظيفة مدير، نتحقق إذا في واحد تاني غير الحالي
        if self.job_title == "manager":
            existing_managers = Employee.objects.filter(job_title="manager")
            if self.pk:
                existing_managers = existing_managers.exclude(pk=self.pk)
            if existing_managers.exists():
                raise ValidationError({"job_title": _("A manager already exists in the system.")})

    def save(self, *args, **kwargs):
        self.full_clean()  # يستدعي clean() تلقائياً
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

#
#
# class Service(models.Model):
#     name = models.CharField(max_length=100, verbose_name="اسم الخدمة")
#     description = models.TextField(verbose_name="وصف الخدمة")
#     image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="صورة الخدمة")
#
#     def __str__(self):
#         return self.name
#
#
#
# class Client(models.Model):
#     name = models.CharField(max_length=100, verbose_name="اسم العميل")
#     description = models.TextField(verbose_name="وصف العميل", blank=True, null=True)
#     image = models.ImageField(upload_to='clients/', verbose_name="صورة العميل", blank=True, null=True)
#     phone = models.CharField(max_length=15, verbose_name="رقم الهاتف", blank=True, null=True)
#     email = models.EmailField(verbose_name="البريد الإلكتروني", blank=True, null=True)
#     website = models.URLField(verbose_name="الموقع الإلكتروني", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
#
#     def __str__(self):
#         return self.name
#
#
#
# class Work(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="العميل")
#     name = models.CharField(max_length=200, verbose_name="اسم المشروع")
#     description = models.TextField(verbose_name="وصف المشروع")
#     image = models.ImageField(upload_to='projects/', verbose_name="صورة المشروع", blank=True, null=True)
#     video = models.FileField(upload_to='projects/videos/', verbose_name="فيديو المشروع", blank=True, null=True)
#     views = models.PositiveIntegerField(default=0, verbose_name="عدد المشاهدات")
#     date = models.DateField(verbose_name="تاريخ تنفيذ المشروع", blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#
#
