from django import forms
from django.forms import TextInput, Textarea

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=200, widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=300, widget=TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Comment
        fields = ['name', 'username', 'email', 'body']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200, widget=TextInput(attrs={'class': 'form-control', 'placeholder':'Chercher'}))

    class Meta:
        fields = ['query']
