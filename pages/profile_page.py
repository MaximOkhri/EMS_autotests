from .base_page import BasePage
from .locators import ProfilePageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import allure
import time

class ProfilePage(BasePage):

    def open_profile_information(self):
        with allure.step("Open profile information"):
            logo = self.browser.find_element(*ProfilePageLocators.LOGO).click()

    def editing_profile_data(self):
        with allure.step("Editing profile data"):
            open_setting_profile = self.browser.find_element(*ProfilePageLocators.OPEN_SEЕTING_PROFILE).click()

            editing_profile_button = self.browser.find_element(*ProfilePageLocators.EDITING_PROFILE_BUTTON).click()

            current_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_PHONE_NUMBER)
            current_phone_number_text = current_phone_number.get_attribute("value")

            if (current_phone_number_text == "+7 962 254 0697"):
                click_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_PHONE_NUMBER).click()
                select_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_PHONE_NUMBER).send_keys(Keys.CONTROL + "a")
                del_old_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_PHONE_NUMBER).send_keys(Keys.DELETE)

                new_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_PHONE_NUMBER).send_keys("9622540698")
            else:
                click_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_PHONE_NUMBER).click()
                select_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_PHONE_NUMBER).send_keys(Keys.CONTROL + "a")
                del_old_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_PHONE_NUMBER).send_keys(Keys.DELETE)

                new_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_PHONE_NUMBER).send_keys("9622540697")

            current_first_name = self.browser.find_element(*ProfilePageLocators.CURRENT_FIRST_NAME)
            current_first_name_text = current_first_name.get_attribute("value")

            if (current_first_name_text == "Иванов"):
                click_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_FIRST_NAME).click()
                select_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_FIRST_NAME).send_keys(Keys.CONTROL + "a")
                del_old_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_FIRST_NAME).send_keys(Keys.DELETE)

                new_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_FIRST_NAME).send_keys("Николаев")
            else:
                click_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_FIRST_NAME).click()
                select_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_FIRST_NAME).send_keys(Keys.CONTROL + "a")
                del_old_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_FIRST_NAME).send_keys(Keys.DELETE)

                new_phone_number = self.browser.find_element(*ProfilePageLocators.CURRENT_FIRST_NAME).send_keys("Иванов")
            
            save_editing_profile_button = self.browser.find_element(*ProfilePageLocators.SAVE_EDITING_PROFILE_BUTTON).click()

            if (current_phone_number_text == "+7 962 254 0697"):
                changed_phone_number = self.browser.find_element(*ProfilePageLocators.CHANGED_PHONE_NUMBER)
                changed_phone_number_text = changed_phone_number.get_attribute("value")
                assert changed_phone_number_text == "+7 962 254 0698", "Номер телефона не изменился"
            else:
                changed_phone_number = self.browser.find_element(*ProfilePageLocators.CHANGED_PHONE_NUMBER)
                changed_phone_number_text = changed_phone_number.get_attribute("value")
                assert changed_phone_number_text == "+7 962 254 0697", "Номер телефона не изменился"

            if (current_first_name_text == "Иванов"):
                changed_first_name = self.browser.find_element(*ProfilePageLocators.CHANGED_FIRST_NAME)
                changed_first_name_text = changed_first_name.get_attribute("value")
                assert changed_first_name_text == "Николаев", "Фамилия не изменилась"
            else:
                changed_first_name = self.browser.find_element(*ProfilePageLocators.CHANGED_FIRST_NAME)
                changed_first_name_text = changed_first_name.get_attribute("value")
                assert changed_first_name_text == "Иванов", "Фамилия не изменилась"
            
    def save_profile_without_editing(self):
        with allure.step("Save profile without editing"):
            open_setting_profile = self.browser.find_element(*ProfilePageLocators.OPEN_SEЕTING_PROFILE).click()

            editing_profile_button = self.browser.find_element(*ProfilePageLocators.EDITING_PROFILE_BUTTON).click()

            assert self.element_is_not_clickable(*ProfilePageLocators.SAVE_EDITING_PROFILE_BUTTON), "Кнопка доступна для нажатия"
