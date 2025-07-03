from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib import admin
from django.utils.html import format_html
from .models import Employee


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    readonly_fields = ('password',)  # ← ده بيخلي الحقل read-only

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'phone_number', 'is_active', 'profile_pic_preview')
    list_filter = ('job_title', 'is_active')
    search_fields = ('full_name', 'job_title', 'phone_number')
    readonly_fields = ('profile_pic_preview', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('user', 'full_name_ar','full_name_en', 'job_title', 'description_ar', 'description_en')
        }),
        ('Contact Info', {
            'fields': ('phone_number', 'address', 'linkedin', 'facebook', 'twitter','instagram','google')
        }),
        ('Profile', {
            'fields': ('profile_picture', 'profile_pic_preview')
        }),
        ('Dates', {
            'fields': ('date_joined', 'is_active', 'created_at', 'updated_at')
        }),
    )

    def profile_pic_preview(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="height: 50px; border-radius: 5px;" />', obj.profile_picture.url)
        return "-"
    profile_pic_preview.short_description = 'Profile Picture Preview'

