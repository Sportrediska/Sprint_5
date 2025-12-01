from selenium.webdriver.common.by import By


class UserRegistrationLocators:
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Вход и регистрация"]')
    NO_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Нет аккаунта"]')
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    INPUT_REPEAT_PASSWORD = (By.NAME, 'submitPassword')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Создать аккаунт"]')
    ERROR_BLOCK_EMAIL = (By.XPATH, '//input[@name="email"]/ancestor::div[contains(@class, "input_inputError__fLUP9")]')
    ERROR_BLOCK_PASSWORD = (By.XPATH, '//input[@name="password"]/ancestor::div[contains(@class, "input_inputError__fLUP9")]')
    ERROR_BLOCK_REPEAT_PASSWORD = (By.XPATH, '//input[@name="submitPassword"]/ancestor::div[contains(@class, "input_inputError__fLUP9")]')
    ERROR_EMAIL = (By.XPATH, './/div/span[@class="input_span__yWPqB" and text()="Ошибка"]')
    USER_NAME = (By.XPATH, './/div/h3[@class = "profileText name"]')
    USER_AVATAR = (By.XPATH, './/button[@class="circleSmall"]')


class UserLoginLocators:
    LOGIN_BUTTON = (By.XPATH, './/div/button[text()="Войти"]')
    LOGOUT_BUTTON = (By.XPATH, './/div/button[text()="Выйти"]')
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    USER_NAME = (By.XPATH, './/div/h3[@class = "profileText name"]')
    USER_AVATAR = (By.XPATH, './/button[@class="circleSmall"]')


class AdLocators:
    ADD_AD_BUTTON = (By.XPATH, './/div/button[text()="Разместить объявление"]')
    AD_POPUP_UNAUTH = (By.XPATH, './/div/form/div/h1[text()="Чтобы разместить объявление, авторизуйтесь"]')
    AD_NAME = (By.NAME, 'name')
    AD_DESCRIPTION = (By.CSS_SELECTOR, 'textarea[name=description]')
    AD_PRICE = (By.NAME, 'price')
    SELECT_AD_CATEGORY_BUTTON = (By.XPATH, '//input[@name="category"]/following-sibling::button')
    AD_CATEGORY_ITEMS = (By.CSS_SELECTOR, '.dropDownMenu_dropMenu__sBxhz:has(input[name="category"]) button.dropDownMenu_btn__o8ARs')
    SELECT_AD_CITY_BUTTON = (By.XPATH, '//input[@name="city"]/following-sibling::button')
    AD_CITY_ITEMS = (By.CSS_SELECTOR, '.dropDownMenu_dropMenu__sBxhz:has(input[name="city"]) button.dropDownMenu_btn__o8ARs')
    AD_ITEM_CONDITION = (By.CLASS_NAME, 'radioUnput_inputRegular__FbVbr')
    AD_BUTTON_PUBLISH = (By.XPATH, './/form[@class="createListing_shell__A5EA7"]/button[@type="submit"]')
    MY_AD_IN_PROFILE = (By.XPATH, '(//div[@class="card"])[last()]//h2')
    LAST_CARD_AD = (By.XPATH, '(//div[@class="card"])')
    AD_ARROW_NEXT = (By.CSS_SELECTOR, '.arrowButton.arrowButton--right')