from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re

# Замена на адрес вашего сайта
URL = "http://62.84.118.232:20002"
# Замена на путь к драйверу вашего браузера

# Инициализация драйвера
driver = webdriver.Chrome()

try:
  # Открытие сайта
  driver.get(URL)
  for i in range(1000000):
  # Ожидание загрузки элемента
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "divColor"))
        )

        initial_url = driver.current_url

        # Получение значения стиля background-color
        style_attribute = element.get_attribute("style")

        color_value = style_attribute.split("background-color: ")[1].strip(";")

        r,g,b = map(int, re.search(
             r'rgb\((\d+),\s*(\d+),\s*(\d+)', color_value).groups())
        color = '#%02x%02x%02x' % (r, g, b)
        print(f"Цвет: {color}")

        # Ожидание загрузки поля ввода
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Insert color']"))
        )

        
        # Ввод шестнадцатеричного цвета в поле ввода
        input_field.clear()  # Очистка поля ввода
        input_field.send_keys(color)

            # Ожидание загрузки кнопки
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][@onclick='sendColor()']"))
        )

        # Нажатие на кнопку
        button.click()

        WebDriverWait(driver, 0.1).until(
        EC.url_changes(initial_url))
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!URL изменился с '{initial_url}' на '{driver.current_url}'")
    except TimeoutException:
        print("Не изменился")

except Exception as e:
  print(f"Ошибка: {e}")

finally:
  # Закрытие браузера
  driver.quit()