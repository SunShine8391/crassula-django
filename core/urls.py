from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Crassula'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.landings.urls')),
    path('', include('apps.seo.urls')),
    path('blog/', include('apps.blog.urls')),
    path('guides/', include('apps.guides.urls')),
    path('', include('apps.boarding.urls')),
    path('', include('apps.pages.urls')),
    path('', include('apps.careers.urls')),
    path('features/', include('apps.features.urls')),
    path('solutions/', include('apps.solutions.urls')),
    path('cases/', include('apps.cases.urls')),
    path('marketplace/', include('apps.marketplace.urls')),
    path('events/', include('apps.events.urls')),
]

if settings.DEBUG:
    urlpatterns += (
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
            static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
