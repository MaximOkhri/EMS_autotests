from EMS_autotests.pages.base_page import BasePage
from EMS_autotests.pages.task_page import TaskPage
from EMS_autotests.pages.employees_page import EmployeePage
from EMS_autotests.pages.locators import MainLink
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import allure

@allure.epic("Test task")
@pytest.mark.task
class TestTask():

    @allure.description("Test create task")
    def test_create_new_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = TaskPage(browser, browser.current_url)
        page.open_task_list()
        page.create_new_task()

    @allure.description("Test add employees to task and replace")
    def test_add_employees_to_task_and_replace(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page = BasePage(browser, browser.current_url)
        page.create_test_employees()
        page = TaskPage(browser, browser.current_url)
        page.open_task_list()
        page.open_task_profile()
        page.add_employees_to_task_and_replace()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page = BasePage(browser, browser.current_url)
        page.delete_test_employees()
    
    @allure.description("Test cancel create task")
    def test_cancel_create_new_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = TaskPage(browser, browser.current_url)
        page.open_task_list()
        page.cancel_create_new_task()

    @allure.description("Test editing task")
    def test_editing_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = TaskPage(browser, browser.current_url)
        page.open_task_list()
        page.open_task_profile()
        page.editing_task()

    @allure.description("Test create empty task")
    def test_create_empty_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = TaskPage(browser, browser.current_url)
        page.open_task_list()
        page.create_empty_task()