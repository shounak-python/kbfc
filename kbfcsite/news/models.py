from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from taggit.managers import TaggableManager


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(5, "Title must be minimum 5 characters long.")])
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through="NewsComments", related_name="comments_author")

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title


class NewsComments(models.Model):
    comment = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.comment