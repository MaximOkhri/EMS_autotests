from EMS_autotests.pages.base_page import BasePage
from EMS_autotests.pages.shift_schedule_page import ShiftSchedulePage
from EMS_autotests.pages.locators import MainLink
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import allure

@allure.epic("Test Schedule")
@pytest.mark.shift_schedule
class TestSchedule():

    @allure.description("Test open employee profile")
    def test_open_employee_profile(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = ShiftSchedulePage(browser, browser.current_url)
        page.open_shift_schedule_page()
        page.open_employee_profile()

    @allure.description("Test close deficit menu")
    def test_close_deficit_menu(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = ShiftSchedulePage(browser, browser.current_url)
        page.open_shift_schedule_page()
        page.close_deficit_menu()
