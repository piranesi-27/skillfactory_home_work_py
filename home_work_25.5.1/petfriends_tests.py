from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *

# pytest -v --driver Chrome petfriends_tests.py


def test_all_pets(login_my_pets):
    """Проверяем на странице 'мои питомцы' наличие питомцев"""
    pytest.driver.implicitly_wait(10)  # неявное ожидание
    # Сохраняем в переменную statistic элементы статистики
    pets_statistic = pytest.driver.find_elements('xpath', '//div[@class=".col-sm-4 left"]')
    # Получаем количество питомцев из данных статистики
    number = pets_statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    # Находим количество питомцев на странице - явное ожидание
    pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))

    # Проверяем, что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == len(pets)

def test_photo_half(login_my_pets):
    """Поверка, что на странице 'мои питомцы' хотя бы у половины карточек есть фото"""

    # Сохраняем в переменную statistic элементы статистики
    statistic = pytest.driver.find_elements("css selector",  ".\\.col-sm-4.left")

    # Сохраняем в переменную images элементы с атрибутом img
    images = pytest.driver.find_elements("css selector", ".table.table-hover img")

    # Количество питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Находим половину от количества питомцев
    half = number // 2

    # Находим количество питомцев с фотографией
    number_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_photos += 1

    # Проверка, что количество питомцев с фотографией больше или равно половине от количества питомцев
    assert number_photos >= half

def test_name_age_and_gender(login_my_pets):
    """Поверка, что на странице 'мои питомцы' у всех питомцев есть имя, возраст и порода"""

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pet_data = pytest.driver.find_elements("css selector", ".table.table-hover tbody tr")

    # Перебираем данные из pet_data, оставляем имя, возраст и породу, остальное изменяем на пустую строку
    # и разделяем пробелом. Находим количество элементов в получившемся списке и сравниваем их
    # с ожидаемым результатом
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)
        assert result == 3


def test_different_names(login_my_pets):
    """Поверяем, что у всех питомцев на странице 'мои питомцы' разные имена """

    # В переменную pet_data сохраняем элементы с данными о питомцах
    pet_data = pytest.driver.find_elements("css selector", ".table.table-hover tbody tr")

    # Перебираем данные из pet_data, оставляем имя, возраст и породу, остальное меняем на пустую строку
    # И разделяем по пробелу. Выбираем имена и добавляем их в список pets_name.
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    # Перебираем имена, если имя повторяется, то прибавляем единицу к счетчику r.
    # Проверяем, если r == 0, то повторяющихся имен нет.
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0

def test_no_duplicate_pets(login_my_pets):
    """Поверка, что на странице 'мои питомцы' нет повторяющихся питомцев"""

    # В переменную pet_data сохраняем элементы с данными о питомцах
    pet_data = pytest.driver.find_elements("css selector", ".table.table-hover tbody tr")

    # Перебираем все данные из pet_data и добавляем в список
    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    line = ''

    # Проверяем на наличие повторяющихся элементов
    for i in list_data:
        line += ''.join(i)
        line += ' '
    list_line = line.split(' ')
    set_list_line = set(list_line)
    a = len(list_line)
    b = len(set_list_line)
    result = a - b
    assert result == 0