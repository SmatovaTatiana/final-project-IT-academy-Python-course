from django.db import models
from django.urls import reverse
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
