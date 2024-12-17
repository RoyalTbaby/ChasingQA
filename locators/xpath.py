import allure
import pytest
import time
from selenium.webdriver.common.by import By


@allure.feature("Wildberries.by Navigation Bar")
class TestWildberries:

    @allure.title("Test#1 - Show Banner")
    @allure.description("The banner with the New Year Sale Wording should appear at the top")
    def test_banner(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the banner unit"):
            banner = driver.find_element(By.XPATH, "//img[@alt='Новогодняя распродажа']")
            assert banner.is_displayed(), "Banner unit is not visible"

    @allure.title("Test#2 - Show Currency Button")
    @allure.description("The button with the current currency should appear at the top")
    def test_currency(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the currency unit"):
            currency = driver.find_element(By.XPATH, "//span[contains(@class, 'simple-menu__currency')]")
            assert currency.is_displayed(), "Currency unit is not visible"

    @allure.title("Test#3 - Show Hamburger Menu")
    @allure.description("The Hamburger Menu should appear at the top")
    def test_menu(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the hamburger unit"):
            menu = driver.find_element(By.XPATH, "//button[contains(@class, 'nav-element__burger')]")
            assert menu.is_displayed(), "Hamburger menu unit is not visible"

    @allure.title("Test#4 - Show Search Panel")
    @allure.description("The search panel should appear at the top")
    def test_search(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the search panel"):
            search = driver.find_element(By.XPATH, "//input[@id='searchInput']")
            assert search.is_displayed(), "Search panel is not visible"

    @allure.title("Test#5 - Show the Logo")
    @allure.description("The logo should appear at the top")
    def test_logo(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the logo unit"):
            logo = driver.find_element(By.XPATH, "//a[contains(@class, 'nav-element__logo')]//img[@alt]")
            assert logo.is_displayed(), "Logo unit is not visible"

    @allure.title("Test#6 - Show the Cart")
    @allure.description("The Cart should appear at the top-right")
    def test_cart(self, driver):
        driver.get("https://www.wildberries.by/")
        time.sleep(3)
        with allure.step("Locate the cart unit"):
            cart = driver.find_element(By.XPATH, "//span[contains(@class, 'navbar-pc__icon--basket')]")
            assert cart.is_displayed(), "Cart unit is not visible"