import time

from selenium.webdriver.common.by import By


def test_login(browser):
    
    browser.get('https://www.saucedemo.com/')
    
    # Ввести логин
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    time.sleep(1)

    # Ввести пароль
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(1)

    # Нажать Enter
    browser.find_element(By.XPATH, '//*[@id="password"]').submit()
    time.sleep(1)
    
    # Валидация авторизации
    browser.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')

    time.sleep(1)