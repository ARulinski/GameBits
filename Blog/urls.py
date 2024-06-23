from django.urls import path
from . import views
from .views import news, article_view, add_article, update_article, delete_article, reviews, guides, pc_view,playstation_view, nintendo_view, xbox_view, add_game, game_detail, game_view
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_image

urlpatterns = [ 
    path("news/", news.as_view(), name="news"),
    path("", views.home, name='home'),
    path('article_view/<int:pk>/', article_view.as_view(), name='article_view'),
    path('add_article/', add_article.as_view(), name='add_article'),
    path('update_article/<int:pk>/', update_article.as_view(), name='update_article'),
    path('delete_article/<int:pk>/', delete_article.as_view(), name='delete_article'),
    path('add_game/', add_game.as_view(), name='add_game'),
    path('game_view', game_view.as_view(), name='game_view'),
    path('game_detail/<int:pk>/', game_detail.as_view(), name='game_detail'),
    path('reviews/', reviews.as_view(), name='reviews'),
    path('guides/', guides.as_view(), name='guides'),
    path('pc_view/', pc_view.as_view(), name='pc_view'),
    path('playstation_view', playstation_view.as_view(), name='playstation_view'),
    path('xbox_view', xbox_view.as_view(), name='xbox_view'),
    path('nintendo_view', nintendo_view.as_view(), name='nintendo_view'),
    path('upload_image/', upload_image, name='upload_image'),


    

    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
