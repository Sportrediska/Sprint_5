from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import AdLocators
from ..locators import UserLoginLocators
from ..locators import UserRegistrationLocators


class TestUserLogout:

    # Logout пользователя
    def test_user_logout_authenticated_user_session_terminated_and_ui_updated(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        driver.find_element(*UserRegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*UserLoginLocators.INPUT_EMAIL).send_keys("test1337@test.ru")
        driver.find_element(*UserLoginLocators.INPUT_PASSWORD).send_keys('1qaz2wsx')
        driver.find_element(*UserLoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserLoginLocators.USER_NAME))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserLoginLocators.USER_AVATAR))

        driver.find_element(*UserLoginLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserLoginLocators.USER_NAME))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserLoginLocators.USER_AVATAR))
        WebDriverWait(driver, 3).until(EC.invisibility_of_element_located(UserRegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON))
        assert True
