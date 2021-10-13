from django import forms
from . import models

"""class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000, widget=forms.Textarea)"""

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Messages
        fields = ('subject', 'name', 'sender_email', 'message')