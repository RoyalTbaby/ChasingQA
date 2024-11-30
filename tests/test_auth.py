import time
import pytest
from selenium.webdriver.common.by import By


def test_login_form(driver):
    driver.get("https://demo.applitools.com/")

    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("admin")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("admin")

    login_button = driver.find_element(By.ID, "log-in")
    login_button.click()

    time.sleep(2)

    assert "ACME" in driver.title, "Error - the login failed!"
