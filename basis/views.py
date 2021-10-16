from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models, forms


# Create your views here.


SUBJECT = ' {name} sent you a message.'
BODY = '{message}'


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


def contacts(request):
    return render(request, 'contacts.html')


def all_portfolio(request):
    portfolios = models.Portfolio.objects.all()
    return render(request, "portfolio/all_portfolio.html",
                  {'portfolios': portfolios})


def contact_form(request):

    sent = False

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = SUBJECT.format(name=cd['name'])
            body = BODY.format(message=cd['message'])
            success = send_mail(subject, body, 'my@mail.com', ['tatsm.reg@gmail.com'])
            if success:
                new_message = form.save(commit=False)
                new_message.name = new_message.name
                new_message.sender_email = new_message.sender_email
                new_message.subject = new_message.subject
                new_message.message = new_message.message
                new_message.save()
                sent = True
    else:
        form = forms.ContactForm()
    return render(request,
                  "contact_form.html",
                  {'form': form, 'sent': sent})


def document_form_upload(request):
    upload = False
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            upload = True
    else:
        form = forms.DocumentForm()
    return render(request,
                  'upload_documents.html',
                  {'form': form, 'upload': upload})
