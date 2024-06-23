import uuid
from django.db import models
from django.forms import DateInput
from users.models import AbstractUser, CustomUser
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


from tinymce.models import HTMLField

# Create your models here.

PLATFORM_CHOICES_DICT = {
    "PC": "PC",
    "PLAYSTATION": "PLAYSTATION",
    "XBOX": "XBOX",
    "NINTENDO": "NINTENDO",
}
PLATFORM_CHOICES = [(key, value) for key, value in PLATFORM_CHOICES_DICT.items()]

TAGS_CHOICES_DICT = {
    "NEWS": "NEWS",
    "LATEST": "LATEST",
    "REVIEWS": "REVIEWS",
    "GUIDE": "GUIDE",
}


class Platform(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'status': 'moderator'})

    def __str__(self):
        return f"{self.name}"

class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    platforms = models.ManyToManyField(Platform)
    date_posted = models.DateTimeField()
    picture = models.ImageField(null=True, blank=True, upload_to='media/images')
    content = HTMLField()
    tag = models.CharField(max_length=20, choices=TAGS_CHOICES_DICT.items(), default="NEWS")
    rating = models.IntegerField(null=True, blank=True, default=None,  help_text='Enter rating from 1 to 5',validators=[MinValueValidator(1), MaxValueValidator(5)]) 

    class Meta:
        ordering = ['-date_posted']
       

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article_view', args=[str(self.pk)])
    
    def save(self, *args, **kwargs):
        if self.tag != "REVIEWS":
            self.rating = None  
        super().save(*args, **kwargs)
    
class Game(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    picture = models.ImageField(null=True, blank=True, upload_to='media/images')
    genre = models.CharField(max_length=300)
    developer = models.CharField(max_length=300)

    class Meta:
        ordering = ['release_date']
       

    def __str__(self):
        return self.title + ' | ' + str(self.genre)
    
    def get_absolute_url(self):
        return reverse('game_view', args=[str(self.pk)])

class Comment(models.Model):
    article =  models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="comments")
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        try:
            return str(self.name) + ' comment ' + str(self.comment_body)

        except:
            return f'Anonymous : {self.comment_body}'

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    reply_body = models.TextField()
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        try:
            return str(self.name) + 'reply' + str(self.reply_body)
        except:
            return f'Anonymus : {self.reply_body}'

