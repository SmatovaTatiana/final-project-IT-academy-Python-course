from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Messages
        fields = ('subject', 'name', 'sender_email', 'message')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.UploadDocument
        fields = ('description', 'document')
