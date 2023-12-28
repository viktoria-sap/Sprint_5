from selenium.webdriver.common.by import By


class Locators:
    PERSONAL_AREA = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Главная страница, кнопка перехода в Личный кабинет
    ENTR_HEADER = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок формы логина
    REG_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Форма логина, гиперссылка для регистрации
    REG_HEADER = (By.XPATH, ".//h2[text()='Регистрация']")  # Заголовок формы регистрации

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::*")  # Инпут имени пользователя
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Инпут e-mail
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::*")  # Инпут пароля

    ERROR_INPUT = (By.CLASS_NAME, "input__error")  # Ошибка заполнения формы регистрации
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации

    ENTR_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка оформления заказа на главной странице

    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт на гл. странице

    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # Гиперссылка для восстановления пароля
    HEADER_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # Хедер формы восстановления пароля
    ENTR_BUTTON_FROM_FORMS = (By.XPATH, "//a[text()='Войти']")  # Кнопка входа в аккаунт на форме восстановления пароля

    HEADER_ACCOUNT_PROFILE = (By.XPATH, ".//a[@href='/account/profile']")  # Заголовок в личном кабинете
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта
    LOGIN_INPUT = (By.XPATH, "//label[text()='Логин']/following-sibling::*")  # Инпут логина в ЛК

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка Конструктор
    LOGO = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']")  # Логотип-гиперссылка

    MAKE_A_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок на главной форме
    BUTTON_SAUCES = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Соусы']")  # Навигация по табам
    HEADER_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")   # Заголовок таба
    BUTTON_FILLINGS = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Начинки']")  # Навигация по табам
    HEADER_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']")  # Заголовок таба
    BUTTON_BUNS = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Булки']")  # Навигация по табам
    HEADER_BUNS = (By.XPATH, ".//h2[text()='Булки']")  # Заголовок таба
