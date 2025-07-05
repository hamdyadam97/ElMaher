from django.urls import path, include

urlpatterns = [
    path('fur/', include('furniture.urls', namespace='furniture')),
    path('user/', include('user.urls', namespace='user')),
    path('', include('section.urls', namespace='section')),
    path('i18n/', include('django.conf.urls.i18n')),
]
