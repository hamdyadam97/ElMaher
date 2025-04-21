from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='employees/', blank=True, null=True)

    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name



class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="صورة الخدمة")

    def __str__(self):
        return self.name



class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم العميل")
    description = models.TextField(verbose_name="وصف العميل", blank=True, null=True)
    image = models.ImageField(upload_to='clients/', verbose_name="صورة العميل", blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name="رقم الهاتف", blank=True, null=True)
    email = models.EmailField(verbose_name="البريد الإلكتروني", blank=True, null=True)
    website = models.URLField(verbose_name="الموقع الإلكتروني", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__(self):
        return self.name



class Work(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="العميل")
    name = models.CharField(max_length=200, verbose_name="اسم المشروع")
    description = models.TextField(verbose_name="وصف المشروع")
    image = models.ImageField(upload_to='projects/', verbose_name="صورة المشروع", blank=True, null=True)
    video = models.FileField(upload_to='projects/videos/', verbose_name="فيديو المشروع", blank=True, null=True)
    views = models.PositiveIntegerField(default=0, verbose_name="عدد المشاهدات")
    date = models.DateField(verbose_name="تاريخ تنفيذ المشروع", blank=True, null=True)

    def __str__(self):
        return self.name



