from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', RedirectView.as_view(url='admin/'), name="admin-site"),
    path('admin/', admin.site.urls),
    path('home/', include('src.apps.core.urls')),
]
urlpatterns += staticfiles_urlpatterns()
