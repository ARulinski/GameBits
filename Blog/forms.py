from django import forms
from .models import Comment,Reply
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'info']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = ['comment_body']
        
        labels = {
            'body': (''),
        }
        
        widgets = {
            'body' : forms.TextInput(),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        
        fields = ['reply_body']
    
        widgets = {
            'body' : forms.TextInput(),
        }      
