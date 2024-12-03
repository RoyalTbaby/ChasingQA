import allure
import pytest
import time
from selenium.webdriver.common.by import By


@allure.feature("Wildberries.by Navigation Bar")
class TestWildberries:

    @allure.title("Test#1 - Show Banner")
    @allure.description("The banner with the Black Friday Wording should appear at the top")
    def test_banner(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the banner unit"):
            banner = driver.find_element(By.CSS_SELECTOR, ".banner img")
            assert banner.is_displayed(), "Banner unit is not visible"

    @allure.title("Test#2 - Show Currency Button")
    @allure.description("The button with the current currency should appear at the top")
    def test_currency(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the currency unit"):
            banner = driver.find_element(By.CSS_SELECTOR, ".simple-menu__currency")
            assert banner.is_displayed(), "Currency unit is not visible"

    @allure.title("Test#3 - Show Humburger Menu")
    @allure.description("The Humburger Menu should appear at the top")
    def test_menu(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the hamburger unit"):
            banner = driver.find_element(By.CSS_SELECTOR, ".nav-element__burger-line")
            assert banner.is_displayed(), "Hamburger menu unit is not visible"

    @allure.title("Test#4 - Show Search Panel")
    @allure.description("The search panel should appear at the top")
    def test_search(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the search panel"):
            banner = driver.find_element(By.CSS_SELECTOR, ".search-catalog__input")
            assert banner.is_displayed(), "Search panel is not visible"

    @allure.title("Test#5 - Show the Logo")
    @allure.description("The logo should appear at the top")
    def test_logo(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the logo unit"):
            banner = driver.find_element(By.CSS_SELECTOR, ".nav-element__logo img")
            assert banner.is_displayed(), "Logo unit is not visible"

    @allure.title("Test#6 - Show the Cart")
    @allure.description("The Cart should appear at the top-right")
    def test_cart(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the cart unit"):
            banner = driver.find_element(By.CSS_SELECTOR, ".navbar-pc__icon--basket")
            assert banner.is_displayed(), "Cart unit is not visible"
