from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Article, Comment, Reply
from .forms import CommentForm, ReplyForm, ArticleForm, ArticleSearchForm
from django.views.generic import FormView
from django.forms import DateInput, inlineformset_factory
from django.db.models import Q

# Create your views here.   
class HomeView(ListView):
    model = Article
    template_name = 'Blog/home.html'  
    context_object_name = 'object_list'
    paginate_by = 10  # Optional: add pagination if needed

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query', None)
        if query:
            queryset = queryset.filter(title__icontains=query)  # Filter by title containing the query
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ArticleSearchForm(self.request.GET or None)  # Pass GET data to form
        context['form'] = form
        return context


class news(ListView):
    model = Article 
    template_name = 'Blog/news.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Article.objects.filter(tag='NEWS')
    
class reviews(ListView):
    model = Article
    template_name = 'Blog/reviews.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Article.objects.filter(tag='REVIEWS')
    
class guides(ListView):
    model = Article
    template_name = 'Blog/guides.html'
    context_object_name = 'guides'

    def get_queryset(self):
        return Article.objects.filter(tag='GUIDE')
    
class pc_view(ListView):
    model = Article
    template_name = 'Blog/pc_view.html'
    context_object_name = 'pc'

    def get_queryset(self):
        return Article.objects.filter(platforms__name='PC')
    
class playstation_view(ListView):
    model = Article
    template_name = 'Blog/playstation_view.html'
    context_object_name ='playstaion'

    def get_queryset(self):
        return Article.objects.filter(platforms__name='PLAYSTATION')

class nintendo_view(ListView):
    model = Article
    template_name = 'Blog/nintendo_view.html'
    context_object_name ='nintendo'

    def get_queryset(self):
        return Article.objects.filter(platforms__name='NINTENDO')
    
class xbox_view(ListView):
    model = Article
    template_name = 'Blog/xbox_view.html'
    context_object_name ='xbox'

    def get_queryset(self):
        return Article.objects.filter(platforms__name='XBOX')

class top_games(ListView):
    model = Article
    template_name = 'Blog/top_games.html'
    context_object_name ='rating'

    def get_queryset(self):
       return Article.objects.filter(rating__gt=4.0)

class article_links(ListView):
    model = Article
    template_name = 'Blog/article_links.html'
    fields = '__all__'


class article_view(DetailView, FormView):
    model = Article
    template_name = 'Blog/article_view.html'
    form_class = CommentForm
    second_form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['form2'] = self.second_form_class()
        context['comments'] = self.get_comments()
        return context
    
    def get_comments(self):
        return Comment.objects.filter(article=self.get_object())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_form' in request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                return self.form_valid(form)
        elif 'reply_form' in request.POST:
            form2 = self.second_form_class(request.POST)
            if form2.is_valid():
                return self.form2_valid(form2)
        return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.name = self.request.user
        comment.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form2_valid(self, form):
        reply = form.save(commit=False)
        parent_comment_id = self.request.POST.get('comment_id')
        parent_reply_id = self.request.POST.get('reply_id')

        if parent_comment_id:
            reply.comment = get_object_or_404(Comment, pk=parent_comment_id)
        elif parent_reply_id:
            parent_reply = get_object_or_404(Reply, pk=parent_reply_id)
            reply.comment = parent_reply.comment  
            

        reply.name = self.request.user
        reply.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('article_view', kwargs={'pk': self.object.pk})
   
class add_article(CreateView):
    model = Article
    template_name = 'Blog/add_article.html'
    form_class = ArticleForm
    
class update_article(UpdateView):
    model = Article
    template_name = 'Blog/update_article.html'
    fields = '__all__'
   

class delete_article(DeleteView):
    model = Article
    template_name = 'Blog/delete_article.html'
    success_url = reverse_lazy('home') 


@csrf_exempt
def upload_image(request):
    if request.method != 'POST' or 'file' not in request.FILES:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    file = request.FILES['file']
    file_name = default_storage.save(file.name, ContentFile(file.read()))
    file_url = default_storage.url(file_name)

    return JsonResponse({'location': file_url})

class SearchResultsView(ListView):
    model = Article
    template_name = 'Blog/search_results.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Article.objects.filter(title__icontains=query)