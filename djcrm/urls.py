from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page, LandingPageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.url', namespace='leads')),
    path('', LandingPageView.as_view(), name='landing-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)