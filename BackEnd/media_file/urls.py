"""
media file app url

"""
from django.conf.urls.static import static

from media_file import views
from mysite import settings

from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()
# ViewSet을 Router에 연결하여 url을 자동으로 맵핑
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
