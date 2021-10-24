import datetime
from datetime import datetime
import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'smatova_project.settings'
application = get_wsgi_application()

import requests

from bs4 import BeautifulSoup

from basis.models import TopNews

NUMBER_OF_NEWS_TO_SHOW = 5


def run_scrapper():
    print("Scrapper. Run scrapper started at ", datetime.now(), '.\n')
    url = "https://dev.by/news"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    news_list = soup.find_all("div", class_="card__body")

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
        except Exception as ex:
            print('Scrapper. ', ex, '\n')

    print("Scrapper. News saved at ", datetime.now(), '.\n')

# run_scrapper()
