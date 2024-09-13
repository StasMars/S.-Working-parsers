from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# коннектимся к браузеру
driver = webdriver.Chrome()

# Коннектимся к урлу категории тг каналов, которые хотим парсить
driver.get('https://tlgrm.ru/channels/finance')

# Прокручиваю страницу вниз range(n) раз
for _ in range(12):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

# Получаю ссылки
urls = [element.get_attribute('href') for element in driver.find_elements(By.CSS_SELECTOR, '.channel-card__subscribe')]


driver.quit()

# сохраняем их в наше файл
with open('Path_to_this_file/file_name.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for url in urls:
        if '@' in url:
            # Извлекаю часть строки после символа '@' и добавляю новый t.me как в db
            tg_channel = url.split('@')[-1]
            formatted_url = f'https://t.me/s/{tg_channel}'
            writer.writerow([formatted_url])