import requests
from bs4 import BeautifulSoup

url = "https://dev.by/news"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
news_list = soup.find_all("div", class_="card__body")
for i in range(5):
    news_element = news_list[i]
    title_element = news_element.find("div", class_="card__title card__title_text-crop")
    links = news_element.find_all("a", class_="card__link")
    for element in links:
        link_url = element["href"]
        link = str(link_url)
        print(title_element.text.strip(), "https://dev.by"+ link +".html", sep='\n')
        print()
