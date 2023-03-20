# Небольшой скрипт по автоматизации VK
# Аутентификация, скролл, нахождение элементов, клики

import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless')

driver = webdriver.Chrome(options=options_chrome)

try:
    driver.maximize_window()
    driver.get("https://vk.com")
    time.sleep(3)
    
    login_form = driver.find_element(By.ID, "index_email")
    login_form.clear()
    login_form.send_keys(os.getenv("LOGIN_VK"))
    login_form.send_keys(Keys.ENTER)
    time.sleep(3)
    
    password_form = driver.find_element(By.NAME, "password")
    password_form.clear()
    password_form.send_keys(os.getenv("PASS_VK"))
    password_form.send_keys(Keys.ENTER)
    time.sleep(3)

    # search_form = driver.find_element(By.ID, "ts_input")
    # search_form.clear()
    # search_form.send_keys("Комарово")
    # search_form.send_keys(Keys.ENTER)
    # time.sleep(6)

    my_page = driver.find_element(By.LINK_TEXT, "Моя страница").click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "VideoPreview-module__videoImage--cPh8B")\
    .click()

except Exception as ex:
    print(ex)
finally:
    time.sleep(10)
    driver.close()
    driver.quit()