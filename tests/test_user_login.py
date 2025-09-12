from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import AdLocators
from ..locators import UserLoginLocators
from ..locators import UserRegistrationLocators


class TestUserLogin:

    # Login пользователя
    def test_user_login_valid_credentials_user_successfully_logged_in(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        driver.find_element(*UserRegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*UserLoginLocators.INPUT_EMAIL).send_keys("test1337@test.ru")
        driver.find_element(*UserLoginLocators.INPUT_PASSWORD).send_keys('1qaz2wsx')
        driver.find_element(*UserLoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserLoginLocators.USER_NAME))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserLoginLocators.USER_AVATAR))
        assert driver.current_url == 'https://qa-desk.stand.praktikum-services.ru/'
