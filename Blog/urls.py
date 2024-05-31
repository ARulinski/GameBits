from django.urls import path
from . import views
from .views import latest, news
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", news.as_view(), name="news"),
    path("latest", latest.as_view(), name="latest"),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)