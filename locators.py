from selenium.webdriver.common.by import By


class UserRegistrationLocators:
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Вход и регистрация"]')
    NO_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Нет аккаунта"]')
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    INPUT_REPEAT_PASSWORD = (By.NAME, 'submitPassword')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Создать аккаунт"]')
    USER_NAME = (By.XPATH, './/div/h3[@class = "profileText name"]')
    USER_AVATAR = (By.XPATH, './/button[@class="circleSmall"]')

# ERROR_BLOCK_EMAIL = //*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/div/div
# ERROR_BLOCK_PASSWORD = 
# ERROR_BLOCK_REPEAT_PASSWORD =
ERROR_EMAIL = (By.XPATH, './/div/span[@class="input_span__yWPqB" and text()="Ошибка"]')

LOGIN_BUTTON = (By.XPATH, './/div/button[text()="Войти"]')
LOGOUT_BUTTON = (By.XPATH, './/div/button[text()="Выйти"]')
ADD_AD_BUTTON = (By.XPATH, './/div/button[text()="Разместить объявление"]')
AD_POPUP_UNAUTH = (By.XPATH, './/div/form/h1[text()="Чтобы разместить объявление, авторизуйтесь"]')
AD_NAME = (By.NAME, 'name')
AD_DESCRIPTION = (By.NAME, 'description')
AD_PRICE = (By.NAME, 'price')

SELECT_AD_CATEGORY_BUTTON = (By.XPATH, './/div/button[@class="dropDownMenu_arrowUp__I25Xq dropDownMenu_noDefault__wSKsP"]')
AD_CATEGORY_ITEMS = (By.CSS_SELECTOR, '.dropDownMenu_dropMenu__sBxhz:has(input[name="category"]) button.dropDownMenu_btn__o8ARs')
SELECT_AD_CITY_BUTTON = (By.XPATH, './/div/button[@class="dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP"]')
AD_CATEGORY_CITY_ITEMS = (By.CSS_SELECTOR, '.dropDownMenu_dropMenu__sBxhz:has(input[name="city"]) button.dropDownMenu_btn__o8ARs')
AD_ITEM_CONDITION = (By.CLASS_NAME, 'radioUnput_inputActive__eC-HY')
AD_BUTTON_PUBLISH = (By.XPATH, './/form[@class="createListing_shell__A5EA7"]/button[@type="submit"]')
MY_AD_IN_PROFILE = (By.XPATH, './/div[@class="profilePage_listningBlock__Fi6E5"]/div/div/div[@class="card"][1]')