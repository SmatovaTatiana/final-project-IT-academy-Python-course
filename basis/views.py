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


def all_experience(request):
    experiences = models.Experience.objects.all()
    return render(request, "experience/all_experience.html",
                  {'experiences': experiences})


def detailed_experience(request, slug, company_name, position):
    experience = get_object_or_404(models.Experience,
                                   slug=slug,
                                   company_name=company_name,
                                   position=position)
    return render(request, "experience/detailed_experience.html",
                  {'experience': experience})


def index_page(request):
    return render(request, 'index.html')
