from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(x))

    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(30)
    browser.quit()