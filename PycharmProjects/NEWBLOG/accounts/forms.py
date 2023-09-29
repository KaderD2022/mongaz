from django import forms
from django.forms import TextInput, Textarea, PasswordInput
from .models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="username", max_length=250, help_text="", required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "id": "Username", "type": "text",
                                                             "placeholder": "user name",
                                                             "data-sb-validations": "required"}))

    first_name = forms.CharField(label="first_name", max_length=250, help_text="", required=True,
                                 widget=forms.TextInput(
                                     attrs={"class": "form-control", "id": "first name", "type": "text",
                                            "placeholder": "first name", "data-sb-validations": "required"}))

    last_name = forms.CharField(label="last_name", max_length=250, help_text="", required=True,
                                widget=forms.TextInput(
                                    attrs={"class": "form-control", "id": "first name", "type": "text",
                                           "placeholder": "last name", "data-sb-validations": "required"}))

    email = forms.CharField(label="email", max_length=250, help_text="", required=True,
                            widget=forms.TextInput(
                                attrs={"class": "form-control", "id": "email", "type": "email", "placeholder": "email",
                                       "data-sb-validations": "required"}))

    password = forms.CharField(label="password", max_length=250, help_text="", required=True,
                               widget=forms.TextInput(
                                   attrs={"class": "form-control", "id": "password", "type": "password",
                                          "placeholder": "password", "data-sb-validations": "required"}))

    confirm_password = forms.CharField(label="confirm_password", max_length=250, help_text="", required=True,
                                       widget=forms.TextInput(
                                           attrs={"class": "form-control", "id": "confirm_password", "type": "password",
                                                  "placeholder": "confirm password",
                                                  "data-sb-validations": "required"}))

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password']


