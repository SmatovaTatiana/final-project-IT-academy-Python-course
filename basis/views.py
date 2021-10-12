from django.shortcuts import render
from . import models

# Create your views here.


def all_education(request):
    educations = models.Education.objects.all()
    return render(request, "education/all_education.html",
                  {'educations': educations})
