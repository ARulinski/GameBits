from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


# Create your views here.
def index(request):
    return render(request, "Blog/index.html")


class latest(ListView):
    model = Article 
    template_name = 'Blog/latest.html'