from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from ckeditor.widgets import CKEditorWidget

# Create your views here.
def home(request):
    return render(request, "Blog/home.html")


class latest(ListView):
    model = Article 
    template_name = 'Blog/latest.html'

class news(ListView):
    model = Article 
    template_name = 'Blog/news.html'


class article_view(DetailView):
    model = Article
    template_name = 'Blog/article_view.html'

class add_article(CreateView):
    model = Article
    template_name = 'Blog/add_article.html'
    fields = '__all__'
    