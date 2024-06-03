from django.urls import path, include
from . import views
from .views import latest, news, article_view, add_article
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_image
from uuid import uuid4

urlpatterns = [
    path("news/", news.as_view(), name="news"),
    path("latest/", latest.as_view(), name="latest"),
    path("", views.home, name='home'),
    path('article_view/<int:pk>/', article_view.as_view(), name='article_view'),
    path("add_article/", add_article.as_view(), name="add_article"),
    path('/upload_image/', upload_image, name='upload_image'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)