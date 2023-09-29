from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    department = models.CharField(max_length=100)
    ville = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)
    geolocation = models.CharField(max_length=255)
    number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.user)


class Visiteur(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
