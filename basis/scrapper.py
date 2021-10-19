# https://stackoverflow.com/questions/8047204/django-script-to-access-model-objects-without-using-manage-py-shell

# https://stackoverflow.com/questions/25537905/django-1-7-throws-django-core-exceptions-appregistrynotready-models-arent-load/26215548#26215548
import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'smatova_project.settings'
application = get_wsgi_application()

import requests

from bs4 import BeautifulSoup

from basis.models import TopNews

NUMBER_OF_NEWS_TO_SHOW = 5


def run_scrapper():
    url = "https://dev.by/news"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    news_list = soup.find_all("div", class_="card__body")
    #articles_list = []

    for i in range(NUMBER_OF_NEWS_TO_SHOW):
        new_article = news_list[i]
        title_element = new_article.find("div", class_="card__title card__title_text-crop")
        link = new_article.find("a", class_="card__link")
        link_url = link["href"]
        link_str = str(link_url)
        new_news = TopNews()
        new_news.title = title_element.text.strip()
        new_news.body = ""
        new_news.link = "https://dev.by" + link_str + ".html"
        new_news.slug = new_news.title.replace(" ", "-")

        try:
            new_news.save()
            print(new_news.title + ' inserted')
            #articles_list.append(new_news)
        except:
            dummy = 0
            print(new_news.title + ' exist in DB')

        #return articles_list
