from django import forms
from django.forms import TextInput,  Textarea

from .models import Comment


class CommentForm(forms.ModelForm):
    username = forms.CharField(max_length=200, widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=300, widget=TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Comment
        fields = ['username', 'email', 'body']

