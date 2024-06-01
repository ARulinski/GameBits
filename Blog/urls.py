from django.urls import path
from . import views
from .views import latest, news, article_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("news", news.as_view(), name="news"),
    path("latest", latest.as_view(), name="latest"),
    path("", views.home, name='home'),
    path('article_view/<int:pk>/', article_view.as_view(), name='article_view'),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)