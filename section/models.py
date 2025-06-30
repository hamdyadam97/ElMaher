from django.db import models
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
        print(self.history_ar)
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
