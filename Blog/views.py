from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Article, Comment, Reply
from .forms import CommentForm, ReplyForm
from django.views.generic import FormView
from django.forms import inlineformset_factory

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
        reply.comment = get_object_or_404(Comment, pk=self.request.POST.get('comment_id'))
        reply.name = self.request.user
        reply.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('article_view', kwargs={'pk': self.object.pk})


   
class add_article(CreateView):
    model = Article
    template_name = 'Blog/add_article.html'
    fields = '__all__'
 
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
