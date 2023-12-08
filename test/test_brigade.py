from EMS_autotests.pages.base_page import BasePage
from EMS_autotests.pages.employees_page import EmployeePage
from EMS_autotests.pages.locators import MainLink
from EMS_autotests.pages.brigades_page import BrigadesPage
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import allure

@allure.epic("Test brigade")
@pytest.mark.brigade
class TestBrigade():

    @allure.description("Test create brigade")
    def test_create_new_brigade(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = BrigadesPage(browser, browser.current_url)
        page.open_brigades_list()
        page.create_new_brigade()

    @allure.description("Test add brigade employees")
    def test_add_brigade_employees(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page = BasePage(browser, browser.current_url)
        page.create_test_employees()
        page = BrigadesPage(browser, browser.current_url)
        page.open_brigades_list()
        page.open_brigade_profile()
        page.add_employees_in_brigade()

    @allure.description("Test delete brigade employee")
    def test_delete_brigade_employee(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()    
        page = BrigadesPage(browser, browser.current_url)
        page.open_brigades_list()
        page.open_brigade_profile()
        page.delete_employees_from_brigade()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page = BasePage(browser, browser.current_url)
        page.delete_test_employees()

    @allure.description("Test cancel create brigade")
    def test_cancel_create_new_brigade(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = BrigadesPage(browser, browser.current_url)
        page.open_brigades_list()
        page.cancel_create_new_brigade()

    @allure.description("Test editing brigade")
    def test_editing_brigade(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = BrigadesPage(browser, browser.current_url)
        page.open_brigades_list()
        page.open_brigade_profile()
        page.editing_brigade()

    @allure.description("Test create empty brigade")
    def test_create_empty_employee(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = BrigadesPage(browser, browser.current_url)
        page.open_brigades_list()
        page.create_empty_brigade()