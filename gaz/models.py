from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gaz(models.Model):
    TYPE_CHOICES = (
        ('b6', 'B6'),
        ('b12', 'B12'),
    )
    ETAT_CHOICES = (
        ('bon', 'Bon'),
        ('moyen', 'Moyen'),
        ('mauvais', 'Mauvais'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(max_length=255)
    color = models.CharField(max_length=55)
    company = models.CharField(max_length=255)
    image = models.CharField(max_length=1000000000)
    price = models.IntegerField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default="b6")
    etat = models.CharField(choices=ETAT_CHOICES, max_length=20, default="bon")
    number_register = models.CharField(max_length=255)

        
    def __str__(self):
        return self.title


class NewGaz(models.Model):
    TYPE_CHOICES = (
        ('b6', 'B6'),
        ('b12', 'B12'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(max_length=255)
    color = models.CharField(max_length=55)
    image = models.CharField(max_length=1000000000)
    company = models.CharField(max_length=255)
    price = models.IntegerField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    number_register = models.CharField(max_length=255)

        
    def __str__(self):
        return self.title


class Commande(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    gaz = models.ForeignKey(Gaz, on_delete=models.CASCADE)
    newgaz = models.ForeignKey(NewGaz, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(max_length=10)
    numero = models.IntegerField()
    adresse_livraison = models.CharField(max_length=255)
    date_livraison = models.DateField()
    date_commande = models.DateTimeField(auto_now_add=True)

