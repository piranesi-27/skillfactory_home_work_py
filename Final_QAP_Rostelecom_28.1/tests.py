from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
from settings import *
import time


'''1. Автотест для тест-кейса RTC-001'''
def test_phone_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_phone_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,'//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email


'''2. Автотест для тест-кейса RTC-002'''
def test_email_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,'//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email

'''3. Автотест для тест-кейса RTC-003'''
def test_login_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-login"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_login)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,'//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email

'''4. Автотест для тест-кейса RTC-004'''
def test_account_number_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-ls"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_account_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,'//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email

'''5. Автотест для авторизации через почту с верной почтой и неверным паролем'''
def test_valid_email_invalid_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(invalid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'

'''6. Автотест для авторизации через почту с неверной почтой и верным паролем'''
def test_invalid_email_valid_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(invalid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'

'''7. Автотест для авторизации через почту с неверной почтой и неверным паролем'''
def test_invalid_email_invalid_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(invalid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(invalid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'

'''8. Автотест для авторизации через почту с пустой почтой и пустым паролем'''
def test_empty_email_empty_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(empty_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(empty_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'

'''9. Автотест для тест-кейса RTС-010'''
def test_lesser_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(lesser_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(lesser_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не менее 8 символов'


'''10. Автотест для тест-кейса RTС-011'''
def test_bigger_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(bigger_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(bigger_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не более 20 символов'

'''11. Автотест для тест-кейса RTС-012'''
def test_cyrillic_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(cyrillic_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(cyrillic_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать только латинские буквы'

'''12. Автотест для тест-кейса RTС-013'''
def test_no_caps_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(no_caps_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(no_caps_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать хотя бы одну заглавную букву'

'''13. Автотест для тест-кейса RTС-014'''
def test_no_numbers_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(no_numbers_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(no_numbers_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

'''14. Автотест для тест-кейса RTС-015'''
def test_empty_phone_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(empty_phone_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,'//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Введите номер телефона'

'''15. Автотест для тест-кейса RTС-016'''
def test_empty_email_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(empty_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,'//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Введите адрес, указанный при регистрации'
