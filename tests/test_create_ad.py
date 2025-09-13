import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import UserLoginLocators, AdLocators, UserRegistrationLocators
from faker import Faker


class TestCreateAd:

    # Создание объявления неавторизованным пользователем
    def test_ad_creation_unauthenticated_user_shows_authorization_modal(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        driver.find_element(*AdLocators.ADD_AD_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AdLocators.AD_POPUP_UNAUTH))

    # Создание объявления авторизованным пользователем
    def test_ad_creation_authenticated_user_ad_published_and_visible_in_profile(self, driver):
        driver.get('https://qa-desk.stand.praktikum-services.ru/')
        driver.find_element(*UserRegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserRegistrationLocators.NO_ACCOUNT_BUTTON))
        driver.find_element(*UserLoginLocators.INPUT_EMAIL).send_keys("test1337@test.ru")
        driver.find_element(*UserLoginLocators.INPUT_PASSWORD).send_keys('1qaz2wsx')
        driver.find_element(*UserLoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserLoginLocators.USER_NAME))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UserLoginLocators.USER_AVATAR))

        driver.find_element(*AdLocators.ADD_AD_BUTTON).click()
        fake = Faker()
        title = fake.sentence()
        description = fake.sentences(5)
        price = fake.random_int(1, 1000)
        driver.find_element(*AdLocators.AD_NAME).send_keys(title)
        driver.find_element(*AdLocators.AD_DESCRIPTION).send_keys(description)
        driver.find_element(*AdLocators.AD_PRICE).send_keys(price)

        driver.find_element(*AdLocators.SELECT_AD_CATEGORY_BUTTON).click()
        random.choice(driver.find_elements(*AdLocators.AD_CATEGORY_ITEMS)).click()

        driver.find_element(*AdLocators.SELECT_AD_CITY_BUTTON).click()
        random.choice(driver.find_elements(*AdLocators.AD_CITY_ITEMS)).click()

        driver.find_element(*AdLocators.AD_ITEM_CONDITION).click()
        driver.find_element(*AdLocators.AD_BUTTON_PUBLISH).click()
        WebDriverWait(driver, 3).until(EC.invisibility_of_element_located(AdLocators.AD_BUTTON_PUBLISH))
        driver.find_element(*UserLoginLocators.USER_AVATAR).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AdLocators.AD_ARROW_NEXT))

        while True:
            next_button = driver.find_element(*AdLocators.AD_ARROW_NEXT)
            if next_button.get_attribute("disabled"):
                break
            next_button.click()
            time.sleep(0.5)
        last_ad_title = driver.find_element(*AdLocators.MY_AD_IN_PROFILE).text
        assert last_ad_title == title
