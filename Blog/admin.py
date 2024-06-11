from django.contrib import admin
from .models import Article, Author, Platform, Comment, Reply

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'subtitle', 'content')
    list_filter = ('author', 'platforms', 'date_posted')
    filter_horizontal = ('platforms',)

admin.site.register(Author)
admin.site.register(Platform)
admin.site.register(Comment)
admin.site.register(Reply)