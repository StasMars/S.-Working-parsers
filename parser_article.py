import requests
from bs4 import BeautifulSoup

# Коннектимся к урлу, который хотим парсить
url = 'url_some_site'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Забираем контент со страницы, который нам нужен
title = soup.find('h1')
content = soup.find_all('div', class_='class_name')

# Выводим его в терминал
print(title.text, '\n')
for p in content:
    print(p.text)


