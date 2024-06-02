from django.urls import path, include
from . import views
from .views import latest, news, article_view, add_article
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("news", news.as_view(), name="news"),
    path("latest", latest.as_view(), name="latest"),
    path("", views.home, name='home'),
    path('article_view/<int:pk>/', article_view.as_view(), name='article_view'),
    path("add_article", add_article.as_view(),name="add_article"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'))
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)