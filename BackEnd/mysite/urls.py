from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include

from app_collect.views import equipments_list
from home.views import hello
from mysite import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path(r'', hello),  # django test
    # path(r'list/', equipments_list, name='equipments_list'),
    path(r"mediaAPI/", include('media_file.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
