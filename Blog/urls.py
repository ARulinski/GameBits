from django.urls import path
from . import views
from .views import news, article_view, add_article, update_article, delete_article, reviews, guides, pc_view,playstation_view, nintendo_view, xbox_view, top_games,article_links
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_image, HomeView, SearchResultsView

urlpatterns = [ 
    path("news/", news.as_view(), name="news"),
    path('', HomeView.as_view(), name='home'),
    path('article_view/<int:pk>/', article_view.as_view(), name='article_view'),
    path('add_article/', add_article.as_view(), name='add_article'),
    path('update_article/<int:pk>/', update_article.as_view(), name='update_article'),
    path('delete_article/<int:pk>/', delete_article.as_view(), name='delete_article'),
    path('reviews/', reviews.as_view(), name='reviews'),
    path('guides/', guides.as_view(), name='guides'),
    path('pc_view/', pc_view.as_view(), name='pc_view'),
    path('playstation_view', playstation_view.as_view(), name='playstation_view'),
    path('xbox_view', xbox_view.as_view(), name='xbox_view'),
    path('nintendo_view', nintendo_view.as_view(), name='nintendo_view'),
    path('upload_image/', upload_image, name='upload_image'),
    path('top_games/', top_games.as_view(), name='top_games'),
    path('article_links/', article_links.as_view(), name='article_links'),
    path('search/', SearchResultsView.as_view(), name='search_results'),


    

    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
