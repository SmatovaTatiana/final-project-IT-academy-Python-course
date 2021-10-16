from django import forms
from django.contrib.auth.models import User

from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Messages
        fields = ('subject', 'name', 'sender_email', 'message')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.UploadDocument
        fields = ('description', 'document')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
