from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from constants import Urls
from locators import Locators


class TestNavigation:

    def test_navigation_personal_area_success(self, driver):
        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.ENTR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.invisibility_of_element(Locators.ENTR_HEADER))

        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON)

        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))

        assert driver.current_url == Urls.PROFILE_FORM_URL

    def test_navigation_personal_area_to_constructor_success(self, driver):
        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.ENTR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))

        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Urls.PROFILE_FORM_URL

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAKE_ORDER_BUTTON))

        assert driver.current_url == Urls.HOME_PAGE_URL


    def test_navigation_personal_area_to_constructor_by_logo_success(self, driver):
        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.ENTR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.invisibility_of_element(Locators.ENTR_HEADER))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))

        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Urls.PROFILE_FORM_URL

        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.MAKE_ORDER_BUTTON))

        assert driver.current_url == Urls.HOME_PAGE_URL

