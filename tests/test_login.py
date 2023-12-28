from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators
from constants import Urls

class TestLogin:
    def test_login_button_enter_account_success(self, driver):
        driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.ENTR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.invisibility_of_element(Locators.ENTR_HEADER))

        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON)


    def test_login_personal_area_success(self, driver):
        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.ENTR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element(Locators.ENTR_HEADER))

        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON)


    def test_login_registration_form_success(self, driver):
        driver.get(Urls.REG_FORM_URL)
        driver.find_element(*Locators.ENTR_BUTTON_FROM_FORMS).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.ENTR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.invisibility_of_element(Locators.ENTR_HEADER))

        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON)

    def test_login_via_forgot_password_valid_credentials_successful(self, driver):
        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))

        driver.find_element(*Locators.BUTTON_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.HEADER_RESTORE_PASSWORD))

        driver.find_element(*Locators.ENTR_BUTTON_FROM_FORMS).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.ENTR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.invisibility_of_element(Locators.ENTR_HEADER))

        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON)
