from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    form = browser.find_element(By.CSS_SELECTOR, """#answer""")
    form.send_keys(y)
    robot_check = browser.find_element(By.CSS_SELECTOR, """[for="robotCheckbox"]""")
    robot_check.click()
    robots_rule = browser.find_element(By.CSS_SELECTOR, """[for="robotsRule"]""")
    robots_rule.click()
    submit = browser.find_element(By.CSS_SELECTOR, """[type="submit"]""")
    submit.click()

finally:
    time.sleep(60)
    browser.quit()
