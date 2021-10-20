from datetime import date
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
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


@login_required  # ограничиваем доступ
def detailed_portfolio(request, slug, project_name):
    portfolio = get_object_or_404(models.Portfolio,
                                  slug=slug,
                                  project_name=project_name)
    return render(request, "portfolio/detailed_portfolio.html",
                  {'portfolio': portfolio})


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


def custom_login(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password'],
            )
            if user is not None:  # используется None, а не if not user т.к. могут быть анонимные юзеры, юзер есть,
                # но прав нет и т.д. Если использовать if user, могут быть проблемы с незакончившими регистрацию и т.д.
                if user.is_active:  # флаг. При нормальной регистрации с уведомлением на почту
                    login(request, user)
                    # from request берутся данные о клиенте и говорится, что это он этот user, после этого он залогинен
                    return HttpResponse('logged in')
                else:
                    return HttpResponse('User not active')
            else:
                return HttpResponse('Bad credentials')

    else:
        form = forms.LoginForm()
    return render(request,
                  'login.html',  # в корне, т.к. к приложению напрямую не относится
                  {'form': form})


def profile(request):
    return render(request, "profile.html", {'user': request.user})


def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()
            models.Profile.objects.create(user=new_user)

            return render(request, "registration_complete.html",
                          {"user": new_user})

    else:
        form = forms.UserRegistrationForm()
        return render(request, "register.html", {'form': form})


def edit_profile(request):
    if request.method == "POST":
        user_form = forms.UserEditForm(request.POST, instance=request.user)
        profile_form = forms.ProfileEditForm(request.POST,
                                             instance=request.user.profile,
                                             )
        if all((user_form.is_valid(), profile_form.is_valid())):
            user_form.save()
            profile_form.save()
            return render(request, "profile.html", {'user': request.user})

    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileEditForm(request.POST, instance=request.user.profile)

    return render(request, "edit_profile.html", {'user_form': user_form,
                                                 'profile_form': profile_form})


def all_news(request):
    today = date.today()
    today_news = models.TopNews.objects.filter(created__gte=today)
    return render(request, "news.html",
                  {'today_news': today_news})
