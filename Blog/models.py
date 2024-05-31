from django.db import models
from users.models import AbstractUser, CustomUser

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
    content = models.TextField()
    tag = models.CharField(max_length=20, choices=TAGS_CHOICES_DICT.items(), default="NEWS")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

