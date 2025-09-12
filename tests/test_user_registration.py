from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import UserRegistrationLocators


class TestUserRegistration:

    # Регистрация пользователя
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

    # Регистрация с email не по маске
    def test_user_registration_invalid_email_format_shows_validation_errors(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        driver.find_element(*UserRegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*UserRegistrationLocators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*UserRegistrationLocators.INPUT_EMAIL).send_keys("incorrect_email")
        driver.find_element(*UserRegistrationLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.ERROR_EMAIL))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.ERROR_BLOCK_EMAIL))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.ERROR_BLOCK_PASSWORD))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.ERROR_BLOCK_REPEAT_PASSWORD))

        email_error_block = driver.find_element(*UserRegistrationLocators.ERROR_BLOCK_EMAIL)
        password_error_block = driver.find_element(*UserRegistrationLocators.ERROR_BLOCK_PASSWORD)
        repeat_password_error_block = driver.find_element(*UserRegistrationLocators.ERROR_BLOCK_REPEAT_PASSWORD)

        email_border = email_error_block.value_of_css_property("border")
        password_border = password_error_block.value_of_css_property("border")
        repeat_password_border = repeat_password_error_block.value_of_css_property("border")

        assert "rgb(255, 105, 114)" in email_border
        assert "rgb(255, 105, 114)" in password_border
        assert "rgb(255, 105, 114)" in repeat_password_border

    # Регистрация существующего пользователя
    def test_user_registration_existing_email_shows_account_exists_error(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        driver.find_element(*UserRegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*UserRegistrationLocators.NO_ACCOUNT_BUTTON).click()


        driver.find_element(*UserRegistrationLocators.INPUT_EMAIL).send_keys('test1337@email.ru')
        driver.find_element(*UserRegistrationLocators.INPUT_PASSWORD).send_keys('1qaz2wsx')
        driver.find_element(*UserRegistrationLocators.INPUT_REPEAT_PASSWORD).send_keys('1qaz2wsx')
        driver.find_element(*UserRegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(UserRegistrationLocators.ERROR_EMAIL))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.ERROR_BLOCK_EMAIL))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.ERROR_BLOCK_PASSWORD))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.ERROR_BLOCK_REPEAT_PASSWORD))

        email_error_block = driver.find_element(*UserRegistrationLocators.ERROR_BLOCK_EMAIL)
        password_error_block = driver.find_element(*UserRegistrationLocators.ERROR_BLOCK_PASSWORD)
        repeat_password_error_block = driver.find_element(*UserRegistrationLocators.ERROR_BLOCK_REPEAT_PASSWORD)

        email_border = email_error_block.value_of_css_property("border")
        password_border = password_error_block.value_of_css_property("border")
        repeat_password_border = repeat_password_error_block.value_of_css_property("border")

        assert "rgb(255, 105, 114)" in email_border
        assert "rgb(255, 105, 114)" in password_border
        assert "rgb(255, 105, 114)" in repeat_password_border