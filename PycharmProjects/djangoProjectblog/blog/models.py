from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('publish', 'PUBLISH'),
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    image = models.CharField(max_length=1000000000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default="draft", max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    name = models.CharField(max_length=400)
    username = models.CharField(max_length=400)
    email = models.EmailField(max_length=400)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    