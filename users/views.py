from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from Blog.forms import  CustomUserCreationForm
# Create your views here.

CustomUser = get_user_model()

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


