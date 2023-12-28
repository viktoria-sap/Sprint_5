from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from constants import Urls
from locators import Locators


class TestExit:

    def test_exit_success(self, driver):
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

        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.ENTR_HEADER))

        assert driver.current_url == Urls.LOGIN_FORM_URL
