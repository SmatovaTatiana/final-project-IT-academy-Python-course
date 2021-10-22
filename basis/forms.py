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


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Pass', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Pass2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('bad password')
        return cd['password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('subscribed_for_mailings', 'subscription_email', )

class MailingForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('subscribed_for_mailings', 'subscription_email', )