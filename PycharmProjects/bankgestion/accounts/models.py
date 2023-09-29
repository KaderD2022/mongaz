from django.db import models

# Create your models here.

class Demande(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    number = models.IntegerField()
    email = models.EmailField()
    date_naissance = models.CharField(max_length=15)
    lieu_naissance = models.CharField(max_length=100)
    image = models.CharField(max_length=10000)

class Client(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    number = models.IntegerField()
    email = models.EmailField()
    date_naissance = models.CharField(max_length=15)
    lieu_naissance = models.CharField(max_length=100)
    image = models.CharField(max_length=10000)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE, related_name='posted'

class Type_accounts(models.Model):
    STATUS_CHOICES = (
        ('courant', 'Courant'),
        ('epargne', 'Epargne'),
        ('bloquée', 'Bloquée'),
    libele = models.CharField(choices=STATUS_CHOICES, default='courant', max_length=20)
        
class Acounts(models.Model):
        pass

    
