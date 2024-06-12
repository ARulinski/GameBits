import uuid
from django.db import models
from users.models import AbstractUser, CustomUser
from django.urls import reverse

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
    "RATING": "RATING",
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

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article_view', args=[str(self.pk)])

class Comment(models.Model):
    article =  models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="comments")
    body = models.CharField(max_length=800)
    date_added = models.DateField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.name.username} {self.body}'
        except:
            return f'Anonymous : {self.body}'


class Reply(models.Model):
    comment_name = models.ForeignKey(Comment, on_delete= models.CASCADE, related_name='replies')
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to= {'status': 'regular', 'status': 'moderator'}, related_name= 'replies' )
    reply_body = models.TextField(max_length=500)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return "by" + " " + str(self.name) + " |  " + "to" + " " + str(self.comment_name.name) + ' : ' + str(self.comment_name.article.title)
    