from django.urls import path
from . import views
from .views import latest, news
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("latest", latest.as_view(), name="latest"),
    path("news", news.as_view(), name="news"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)