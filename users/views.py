from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect   
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from Blog.forms import  CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

CustomUser = get_user_model()

class profile_view(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/profile_view.html"
    context_object_name = 'user'    

    def get_object(self):
        return self.request.user
    
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['first_name','last_name', 'email', 'info', 'avatar']  # Specify the fields that can be updated
    template_name = 'users/update_profile.html'  # Template to render
    success_url = reverse_lazy('profile_view')  # URL to redirect after successful update

    def get_object(self, queryset=None):
        # Ensure the view updates the currently logged-in user's profile
        return self.request.user

class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'users/delete_profile.html'
    success_url = reverse_lazy('home')  # Redirect after successful deletion

    def get_object(self, queryset=None):
        # Ensure that the view deletes the currently logged-in user's profile
        return get_object_or_404(CustomUser, pk=self.request.user.pk)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        # Optionally, handle post-deletion actions here
        return response




def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register_view.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
           
            return redirect('news')
            
        else:
         
            return redirect('login_view')
   


    return render (request, "users/login_view.html")

def logout_user(request):
    logout(request)
    return redirect('news')


