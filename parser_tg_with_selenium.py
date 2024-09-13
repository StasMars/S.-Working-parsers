from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# Открываем страницу
driver.get('https://t.me/s/some_tg_channal')

# Прокручиваю страницу вверх range(n) раз
for _ in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
    time.sleep(2)

# Получаю текст всех сообщений
articles = [element.text for element in driver.find_elements(By.CSS_SELECTOR, '.tgme_widget_message_text')]


driver.quit()

# Вывожу все спарсенные сообщения в терминал
for a in articles:
    print(a)