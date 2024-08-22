import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    print("quiting browser")
    browser.quit()


@pytest.fixture()
def auth(browser, request):

    browser.implicitly_wait(10)

    link = f"https://stepik.org/lesson/{request.param}/step/1"
    # загрузка страницы
    browser.get(link)

    # логин в пользователя
    browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button").click()
    browser.find_element(By.ID, "id_login_email").send_keys("********@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("********")
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

    time.sleep(5)

    yield browser


@pytest.mark.parametrize("auth", [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905], indirect=True)
def test_resolver(auth):
    try:
        auth.find_element(By.CSS_SELECTOR, ".again-btn").click()
    except Exception:
        pass
    finally:

        auth.find_element(By.CSS_SELECTOR, ".ember-text-area").send_keys(str(math.log(int(time.time()))))
        auth.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        answer = auth.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        print(answer, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        assert answer == "Correct!"

# try for github
