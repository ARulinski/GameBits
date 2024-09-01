from django import forms
from .models import Comment,Reply, Article
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
        fields = ["comment_body"]


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_body']


class DateInput(forms.DateInput):
    input_type = 'date'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'date_posted': DateInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.tag != 'NEWS':
            self.fields['rating'].widget = forms.HiddenInput()

class ArticleSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label="Search Articles",
        widget=forms.TextInput(attrs={
            'placeholder': 'Search articles, reviews, guides...',
            'class': 'search-input',  # Matches your CSS styles
        })
    )

      
        