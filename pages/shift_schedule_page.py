from .base_page import BasePage
from .locators import ShiftSchedulePageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import allure
import time

class ShiftSchedulePage(BasePage):

    def open_shift_schedule_page(self):
        with allure.step("Open shift schedule page"):
            click_schedule_page = self.browser.find_element(*ShiftSchedulePageLocators.SCHEDULE_PAGE).click()

    def open_employee_profile(self):
        with allure.step("Open employee profile"):

            click_on_employee = self.browser.find_element(*ShiftSchedulePageLocators.EMPLOYEE_BUTTON).click()
            time.sleep(2)

            get_url = str(self.browser.current_url)
            assert get_url.__contains__("https://ems.biacorp.ru/employees/"), "Не выполнился переход в профиль сотрудника"

    def close_deficit_menu(self):
        with allure.step("Close deficit menu"):
            click_on_deficit_menu = self.browser.find_element(*ShiftSchedulePageLocators.DEFICIT_MENU_BUTTON).click()
            click_on_x_button = self.browser.find_element(*ShiftSchedulePageLocators.X_BUTTON).click()
            time.sleep(1)

            assert self.is_not_element_present(*ShiftSchedulePageLocators.DEFICIT_MENU), "Меню не закрыто"

            click_on_deficit_menu = self.browser.find_element(*ShiftSchedulePageLocators.DEFICIT_MENU_BUTTON).click()
            click_on_cancel_button = self.browser.find_element(*ShiftSchedulePageLocators.CANCEL_BUTTON).click()
            time.sleep(1)

            assert self.is_not_element_present(*ShiftSchedulePageLocators.DEFICIT_MENU), "Меню не закрыто"
