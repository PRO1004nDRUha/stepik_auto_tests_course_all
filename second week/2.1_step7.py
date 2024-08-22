from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return math.log(abs(12*math.sin(x)))


try:

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(int(x))

    browser.find_element(By.ID, "answer").send_keys(str(y))

    browser.find_element(By.ID, "robotCheckbox").click()

    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.CSS_SELECTOR, ".btn").click()
finally:
    time.sleep(30)
    browser.quit()
