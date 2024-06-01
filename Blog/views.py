from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


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