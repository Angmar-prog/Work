import requests
from bs4 import BeautifulSoup

url = 'https://ria.ru/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#Вывод главных новостей
news = soup.find_all('div', class_='cell-main-photo__title')
time = soup.find_all('div', class_='cell-main-photo__info')

for i in range(len(news)):
    print(f"{news[i].text.strip()} - {time[i].text.strip()}")

#Вывод не главных новостей
news = soup.find_all('span', class_='cell-list__item-title')
time = soup.find_all('div', class_='cell-list__item-info')

for i in range(len(news)):
    print(f"{news[i].text.strip()} - {time[i].text.strip()}")