from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fur/', include('furniture.urls',namespace='furniture')),
    path('user/', include('user.urls',namespace='user')),
    path('', include('section.urls',namespace='section')),
]
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),  # هذا لتفعيل تبديل اللغة
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

