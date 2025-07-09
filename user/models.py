from django.utils.translation import gettext_lazy as _, get_language
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):
    image = models.ImageField(_("Profile Picture"), upload_to='user/', blank=True, null=True)
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

    class Meta:
        verbose_name = _("المستخدم")
        verbose_name_plural = _("المستخدمين")


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
        verbose_name = _("الموظفين")
        verbose_name_plural = _("الموظفين")

