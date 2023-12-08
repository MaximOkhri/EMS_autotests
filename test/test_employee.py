from EMS_autotests.pages.base_page import BasePage
from EMS_autotests.pages.employees_page import EmployeePage
from EMS_autotests.pages.locators import MainLink
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import allure

@allure.epic("Test employees")
@pytest.mark.employee
class TestEmployees():

    @allure.description("Test create employee")
    def test_create_employee(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page.create_new_employee()

    @allure.description("Test cancel create employee")
    def test_cancel_choice_of_method_add_manually(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page.cancel_choice_of_method_add_manually()

    @allure.description("Test cancel create employee")
    def test_cancel_create_new_employee(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page.cancel_create_new_employee()

    @allure.description("Test editing employee")
    def test_editing_employee(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page.open_employee_profile()
        page.editing_employee()

    @allure.description("Test create empty employee")
    def test_create_empty_employee(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page.create_empty_employee()