from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConstructor:
    def test_constructor_buns(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAKE_A_BURGER))

        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        assert driver.find_element(*Locators.HEADER_FILLINGS).is_displayed()

        driver.find_element(*Locators.BUTTON_BUNS).click()
        assert driver.find_element(*Locators.HEADER_BUNS).is_displayed()

    def test_constructor_to_sauces(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAKE_A_BURGER))

        driver.find_element(*Locators.BUTTON_SAUCES).click()
        assert driver.find_element(*Locators.HEADER_SAUCES).is_displayed()

    def test_constructor_to_fillings(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAKE_A_BURGER))

        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        assert driver.find_element(*Locators.HEADER_FILLINGS).is_displayed()
        