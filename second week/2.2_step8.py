from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    line = """http://suninjuly.github.io/file_input.html"""
    browser = webdriver.Chrome()
    browser.get(line)

    browser.find_element(By.CSS_SELECTOR, """[name="firstname"]""").send_keys("""Andrew""")
    browser.find_element(By.CSS_SELECTOR, """[name="lastname"]""").send_keys("""Karavaev""")
    browser.find_element(By.CSS_SELECTOR, """[name="email"]""").send_keys("""mail@gmail.com""")
    way = os.path.join(os.path.abspath(os.path.dirname(__file__)), "text.txt")
    browser.find_element(By.ID, """file""").send_keys(way)
    browser.find_element(By.CLASS_NAME, """btn""").click()
finally:
    time.sleep(30)
    browser.quit()
