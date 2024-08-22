from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    link = """http://suninjuly.github.io/alert_accept.html"""
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, """btn""").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.ID, """input_value""").text)
    y = calc(x)
    browser.find_element(By.ID, """answer""").send_keys(str(y))
    browser.find_element(By.CLASS_NAME, """btn""").click()
finally:
    time.sleep(30)
    browser.quit()