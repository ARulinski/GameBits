from django import forms
from .models import Comment, Reply
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
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Write your comment here...'}),
        }
        labels = {
            'body': ''
        }
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_body']  # Assuming 'reply_body' is the field name in your Reply model
        widgets = {
            'reply_body': forms.Textarea(attrs={'placeholder': 'Write your reply here...'}),
        }
        labels = {
            'reply_body': ''
        }