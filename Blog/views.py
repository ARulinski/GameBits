from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your views here.   
def home(request):
    return render(request, "Blog/home.html")

def reviews(request):
    return render(request, "Blog/reviews.html")


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

def cart(request):
             pass

@csrf_exempt
def upload_image(request):
    if request.method != 'POST' or 'file' not in request.FILES:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    file = request.FILES['file']
    file_name = default_storage.save(file.name, ContentFile(file.read()))
    file_url = default_storage.url(file_name)

    return JsonResponse({'location': file_url})
    
    


    
