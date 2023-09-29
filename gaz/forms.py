from django.forms import ModelForm
from . import models
from .models import Order
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Commande
        fields = ('nom', 'email', 'address', 'vile', 'pays', 'zipcode') 
