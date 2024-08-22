from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    link = """http://suninjuly.github.io/explicit_wait2.html"""
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, """price"""), """100"""))
    browser.find_element(By.ID, """book""").click()

    x = int(browser.find_element(By.ID, """input_value""").text)
    y = calc(x)
    browser.find_element(By.ID, """answer""").send_keys(str(y))
    browser.find_element(By.ID, """solve""").click()
finally:
    time.sleep(30)
    browser.quit()
