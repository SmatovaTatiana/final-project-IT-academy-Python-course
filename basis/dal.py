# To access Django
import datetime
import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'smatova_project.settings'
application = get_wsgi_application()

from django.utils import timezone

from datetime import date
from basis import models
from basis.models import Profile


def get_recipients():
    emails = []
    subscribers = Profile.objects.filter(subscribed_for_mailings=True)
    for subscriber in subscribers:
        emails.append(subscriber.subscription_email)
    return emails


def get_content():
    articles = []
    news = ""
    today = date.today()
    today_news = models.TopNews.objects.filter(created__gte=today)

    for article in today_news:
        articles.append([article.title, article.body, article.link])

    for outer_list in articles:
        for inner_list in outer_list:
            news = news + ', ' + inner_list

    return news
content = get_content()
# recipients = get_recipients()
