from django.db import models

# Create your models here.
from django.urls import reverse


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
