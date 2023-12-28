from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from constants import Urls
from locators import Locators

faker = Faker()

class TestRegistration:
    def test_registration_success(self, driver):
        name = faker.first_name()
        email = faker.email()

        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))
        assert driver.current_url == Urls.LOGIN_FORM_URL

        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_HEADER))

        # Регистрация
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))
        assert driver.current_url == Urls.LOGIN_FORM_URL

        # Проверка регистрации через авторизацию
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.ENTR_BUTTON).click()

        # Ожидание загрузки страницы
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAKE_A_BURGER))

        # Переход в ЛК и сверка кредов
        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))

        assert driver.find_element(*Locators.LOGIN_INPUT).get_attribute('value') == email

    def test_registration_failure(self, driver):
        name = faker.first_name()
        email = faker.email()

        driver.find_element(*Locators.PERSONAL_AREA).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ENTR_HEADER))
        assert driver.current_url == Urls.LOGIN_FORM_URL

        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REG_HEADER))

        # Регистрация
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.INCORRECT_PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()

        assert driver.find_element(*Locators.ERROR_INPUT).text == 'Некорректный пароль'




