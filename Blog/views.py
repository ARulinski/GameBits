from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Article, Comment
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import CommentForm


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

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['commentform'] = CommentForm()
            return context
        
        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            commentform = CommentForm(request.POST)
            if commentform.is_valid():
                comment = commentform.save(commit=False)
                comment.name = request.user
                comment.article = self.object
                comment.save()
                return redirect('article_view', pk=self.object.pk)
            
            context = self.get_context_data()
            context['commentform'] = commentform
            return render(request, self.template_name, context)





        


class add_article(CreateView):
    model = Article
    template_name = 'Blog/add_article.html'
    fields = '__all__'


@csrf_exempt
def upload_image(request):
    if request.method != 'POST' or 'file' not in request.FILES:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    file = request.FILES['file']
    file_name = default_storage.save(file.name, ContentFile(file.read()))
    file_url = default_storage.url(file_name)

    return JsonResponse({'location': file_url})
    
    


    
