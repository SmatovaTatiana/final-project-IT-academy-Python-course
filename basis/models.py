from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Education(models.Model):
    graduated = models.PositiveSmallIntegerField()
    school_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    certificate = models.ImageField(blank=True)
    slug = models.SlugField(max_length=255, unique='course_name')

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('basis:detailed_education',
                       args=[self.slug,
                             self.graduated,
                             ])


class Experience(models.Model):
    start_date = models.PositiveSmallIntegerField()
    end_date = models.PositiveSmallIntegerField()
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    industry = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique='company_name')

    def __str__(self):
        return self.position

    def get_absolute_url(self):
        return reverse('basis:detailed_experience',
                       args=[self.slug,
                             self.company_name,
                             self.position
                             ])


class Portfolio(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    slug = models.SlugField(max_length=255, unique='project_name')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse('basis:detailed_portfolio',
                       args=[self.slug,
                             self.project_name])


class Messages(models.Model):
    name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    message = models.CharField(max_length=1000)
    subject = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sender_email


class UploadDocument(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    file_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    hr = models.BooleanField(default=False)
    subscribed_for_mailings = models.BooleanField(default=False)
    subscription_email = models.EmailField(default="")

    def __str__(self):
        return str(self.user)


class TopNews(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    link = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, unique='project_name', default='')
