from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    line = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(line)
    x = browser.find_element(By.ID, """input_value""").text
    y = calc(int(x))
    browser.execute_script("""window.scrollBy(0, 100);""")
    browser.find_element(By.ID, """answer""").send_keys(str(y))
    browser.find_element(By.ID, """robotCheckbox""").click()
    browser.find_element(By.ID, """robotsRule""").click()
    browser.find_element(By.CLASS_NAME, """btn""").click()

finally:
    time.sleep(30)
    browser.quit()
