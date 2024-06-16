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
        context = super(article_view,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        self.obejct = self.get_object
        if 'form' in request.POST:
            form_class = self.form_class
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)

        if form_name == 'form' and form.is_valid():
            print('returned comment ')
            return self.form_valid(form)
        elif form_name == 'form2' and form.is_valid():
            print("returned reply")
            return self.form2.valid(form)
    
    def get_success_url(self):
        self.object = self.get_object()
        article = self.object.article
        title = self.object.title
        return reverse_lazy("article_view", kwargs ={
            'article': article.slug,
            'title' : title.slug })
    
    def form_valid(self, form):
        self.obejct = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.article_name = self.object.comments.name
        fm.article_name_id = self.obejct.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.name = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

   
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
