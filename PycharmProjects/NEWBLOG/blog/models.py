from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_posts')
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=100000)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
    publish = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')
    objects = models.Manager
    published: PublishedManager = PublishedManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title


class Reponse(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='recomment')
    name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment.name


