from api import PetFriends
from settings import valid_email, valid_password, invalid_password, invalid_email, invalid_key
import os


pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""
    status, result = pf.get_api_key(email, password) # сохраняем результат запроса в переменные
    assert status == 200 # проверяем ответ запроса
    assert 'key' in result # проверяем что апи ключ получен

def test_all_pets_with_valid_key(filter=''):
    """ Проверяем что система возвращает спиосок питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_email)
    status, result = pf.get_list_of_pets(auth_key, filter) # сохраняем список питомцев в переменные для дальнейшей проверки
    assert status == 200
    assert len(result['pets']) > 0 # проверяем что в списке питомцев есть значения

def test_adding_new_pet_with_valid_key(name='Barsik', animal_type='Cat', age='5', pet_photo='images/cats.jpg'):
    """ Добавляем нового питомца через api/pets"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo) # добавляем фото с помощью библиотеки os
    _, auth_key = pf.get_api_key(valid_email, valid_email)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name # проверяем что имя нового питомца совпадает в введнныем занчением


def test_update_info_with_valid_key(name='Murzik', animal_type='', age=''):
    """ Обновляем инфу о питомце"""
    _, auth_key = pf.get_api_key(valid_email, valid_email)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets') # создаем переменную куда помещаем список наших питомцев

    if len(my_pets['pets']) > 0: # если в списке есть питомце
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age) # то обновляем информацию питомца по индексу

    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """ Удаляем питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0: # если в списке нет питомцев то добавляем нового
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()



######## задание 19.7.2 ############


def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """1. Проверяем ответ запроса с неверным логином и паролем"""
    status, result = pf.get_api_key(email, password) # сохраняем результат запроса в переменные
    assert status == 403 # проверяем что система верно выдает ошибку

def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    """2. Проверяем ответ запроса с неверным логином """
    status, result = pf.get_api_key(email, password) # сохраняем результат запроса в переменные
    assert status == 403 # проверяем что система верно выдает ошибку

def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    """3. Проверяем ответ запроса с неверным паролем """
    status, result = pf.get_api_key(email, password) # сохраняем результат запроса в переменные
    assert status == 403 # проверяем что система верно выдает ошибку

def test_adding_new_pet_simple_valid_key(name='Paolo', animal_type='Dog', age='5'):
    """4. Добавляем нового питомца через простую форму api/create_new_pet"""
    _, auth_key = pf.get_api_key(valid_email, valid_email)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name # проверяем что имя нового питомца совпадает в введнныем занчением

def test_add_photo_pet(pet_photo='images/cats.jpg'):
    """5. Добавляем или меняем фотографию существующего питомца"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert "pet_photo" in result
    else:
        raise Exception("There is no my Pets")

def test_all_pets_with_invalid_key(filter=''):
    """6. Проверяем что система НЕ возвращает список питомцев с неверным апи ключом"""
    _, auth_key = (200, {'key': invalid_key})
    status, result = pf.get_list_of_pets(auth_key, filter) # сохраняем список питомцев в переменные для дальнейшей проверки
    assert status == 403

def test_adding_new_pet_with_invalid_key(name='Barsik', animal_type='Cat', age='3', pet_photo='images/cats.jpg'):
    """7. Проверяем что нельзя добавить нового питомца через api/pets с неверным апи ключом"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo) # добавляем фото с помощью библиотеки os
    _, auth_key = (200, {'key': invalid_key})
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403

def test_adding_empty_new_pet_simple_valid_key(name='', animal_type='', age=''):
    """8. Добавляем нового питомца через простую форму api/create_new_pet без данных"""
    _, auth_key = pf.get_api_key(valid_email, valid_email)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name # проверяем что имя нового питомца совпадает с введнным занчением

def test_update_wrong_age_info_with_valid_key(name='', animal_type='', age='@@@@'):
    """9. Обновляем возраст питомца с неверными данными"""
    _, auth_key = pf.get_api_key(valid_email, valid_email)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets') # создаем переменную куда помещаем список наших питомцев

    if len(my_pets['pets']) > 0: # если в списке есть питомце
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][2]['id'], name, animal_type, age) # то обновляем информацию питомца по индексу

    assert status == 200
    assert result['age'] == age

def test_get_pets_with_invalid_filter(filter='рандомный_фильтр'):
    """10. Проверяем невозможность получения список питомцев с неверным фильтром"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 500

