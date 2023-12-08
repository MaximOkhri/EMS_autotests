from EMS_autotests.pages.base_page import BasePage
from EMS_autotests.pages.directories_page import DirectoriesPage
from EMS_autotests.pages.employees_page import EmployeePage
from EMS_autotests.pages.profile_page import ProfilePage
from EMS_autotests.pages.task_page import TaskPage
from EMS_autotests.pages.locators import MainLink
from EMS_autotests.pages.create_directories_page import CreateDirectoriesPage
from EMS_autotests.pages.edit_directories_page import EditDirectoriesPage
from EMS_autotests.pages.delete_durectories_page import DeleteDirectoriesPage
from EMS_autotests.pages.brigades_page import BrigadesPage
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import allure

@allure.epic("Test delete function")
@pytest.mark.delete
class TestDelete():

    @allure.description("Test delete brigade")
    def test_delete_brigade(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = BrigadesPage(browser, browser.current_url)
        page.open_brigades_list()
        page.open_brigade_profile()
        page.delete_brigade()
    
    @allure.description("Test delete employee")
    def test_delete_employee(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = EmployeePage(browser, browser.current_url)
        page.open_employee_list()
        page.open_employee_profile()
        page.delete_employee()
    
    @allure.description("Test delete object")
    def test_delete_object(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_object_list()
        page.open_object_profile()
        page = DeleteDirectoriesPage(browser, browser.current_url)
        page.delete_object()
    
    @allure.description("Test delete task")
    def test_delete_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_tasks_list()
        page.open_task_profile()
        page = DeleteDirectoriesPage(browser, browser.current_url)
        page.delete_task()

    @allure.description("Test delete qualification")
    def test_delete_qualification(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_qualification_list()
        page.open_qualification_profile()
        page = DeleteDirectoriesPage(browser, browser.current_url)
        page.delete_qualification()

    @allure.description("Test delete shift")
    def test_delete_shift(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_shift_list()
        page.open_shift_profile()
        page = DeleteDirectoriesPage(browser, browser.current_url)
        page.delete_shift()

    @allure.description("Test delete task")
    def test_delete_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = TaskPage(browser, browser.current_url)
        page.open_task_list()
        page.open_task_profile()
        page.delete_task()