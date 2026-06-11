from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/groom/', permanent=False)),
    path('admin/', admin.site.urls),
    path('groom/', include('groom.urls')),
    path('guests/', include('guests.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
