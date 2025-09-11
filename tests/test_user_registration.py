from selenium.webdriver.common.by import By
from locators import UserRegistrationLocators
import time
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUserRegistration:
    
    #Регистрация пользователя
    def test_user_registration_valid_data_user_created_and_logged_in(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        driver.find_element(*UserRegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*UserRegistrationLocators.NO_ACCOUNT_BUTTON).click()

        fake = Faker()
        email = fake.email()
        password = fake.password()

        driver.find_element(*UserRegistrationLocators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*UserRegistrationLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*UserRegistrationLocators.INPUT_REPEAT_PASSWORD).send_keys(password)

        driver.find_element(*UserRegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.USER_NAME))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.USER_AVATAR))
        assert driver.current_url == 'https://qa-desk.stand.praktikum-services.ru/'
    
    #Регистрация с email не по маске
    def test_user_registration_invalid_email_format_shows_validation_errors(self):
        pass
    
    #Регистрация существующего пользователя
    def test_user_registration_existing_email_shows_account_exists_error(self):
        pass

