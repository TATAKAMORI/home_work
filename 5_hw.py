from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://saucedemo.com/')

# Поиск элемента
username = driver.find_element(By.CSS_SELECTOR, '#user-name')
if username is None:
    print('Элемент не найден')
else:
    print('Элемент найден')


password = driver.find_element(By.CSS_SELECTOR, '#password')
if password is None:
    print('Элемент не найден')
else:
    print('Элемент найден')


submit = driver.find_element(By.CSS_SELECTOR, '#login-button')
if submit is None:
    print('Элемент не найден')
else:
    print('Элемент найден')