from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models

# Create your views here.


def all_education(request):
    educations = models.Education.objects.all()
    return render(request, "education/all_education.html",
                  {'educations': educations})


def detailed_education(request, slug, graduated):
    education = get_object_or_404(models.Education,
                                  slug=slug,
                                  graduated=graduated)
    return render(request, "education/detailed_education.html",
                  {'education': education})
