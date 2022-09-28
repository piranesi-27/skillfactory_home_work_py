import pytest
from selenium import webdriver
from settings import *


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.set_headless(True)
    chrome_options.add_argument('--headless')
    return chrome_options


@pytest.fixture(autouse=True)
def login_my_pets():
   pytest.driver = webdriver.Chrome()
   #Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   pytest.driver.find_element('id','email').send_keys(email)
   # Вводим пароль
   pytest.driver.find_element('id','pass').send_keys(password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element('css selector','button[type="submit"]').click()
   pytest.driver.find_element('link text', 'Мои питомцы').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element('tag name','h2').text == username

   yield

   pytest.driver.quit()

