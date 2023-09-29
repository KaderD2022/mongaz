from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categorys(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)


class Post(models.Model):
    categorys = models.ForeignKey(Categorys, on_delete=models.CASCADE, related_name="categorys")
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('publish', 'PUBLISH'),
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default="draft", max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
