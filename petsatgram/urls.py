from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import petsatgram

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petsatgram.main.urls')),
    path('profile/', include('petsatgram.profile_app.urls')),
    path('photo/', include('petsatgram.photo.urls')),
    path('pet/', include('petsatgram.pet.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'petsatgram.main.views.show404'
