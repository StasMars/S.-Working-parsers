import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv

# Коннектимся к урлу категории тг каналов, которые хотим парсить
url = 'https://tlgrm.ru/channels/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# берем хпас ссылок на эти каналы
dom = etree.HTML(str(soup))
urls = dom.xpath('//a[@class="channel-card__subscribe"]/@href')

# сохраняем их в наше файл
with open('Path_to_this_file/file_name.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for url in urls:
        writer.writerow([url])

