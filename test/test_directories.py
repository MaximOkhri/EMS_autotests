from EMS_autotests.pages.base_page import BasePage
from EMS_autotests.pages.directories_page import DirectoriesPage
from EMS_autotests.pages.locators import MainLink
from EMS_autotests.pages.create_directories_page import CreateDirectoriesPage
from EMS_autotests.pages.edit_directories_page import EditDirectoriesPage
from EMS_autotests.pages.delete_durectories_page import DeleteDirectoriesPage
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import allure

@allure.epic("Tests directories")
@pytest.mark.directories
class TestDirectories():

    @allure.description("Open objects list")
    def test_open_object_list(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_object_list()
        
    @allure.description("Open tasks list")
    def test_open_task_list(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_task_list()

    @allure.description("Open qualifications list")
    def test_open_qualification_list(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_qualification_list()

    @allure.description("Open shifts list")
    def test_open_shift_list(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_shift_list()

@allure.epic("Test create directories function")
@pytest.mark.create
class TestCreateDirectories():

    @allure.description("Test create object")
    def test_create_object(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_object_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.create_new_object()

    @allure.description("Test create empty object")
    def test_create_empty_object(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_object_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.create_empty_object()

    @allure.description("Test create empty task")
    def test_create_empty_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_tasks_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.create_empty_task()

    @allure.description("Test create empty qualification")
    def test_create_empty_qualification(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_qualification_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.create_empty_qualification()

    @allure.description("Test create empty shift")
    def test_create_empty_shift(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_shift_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.create_empty_shift()

    @allure.description("Test create task")
    def test_create_type_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_tasks_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.create_new_type_task()

    @allure.description("Test create qualification")
    def test_create_qualification(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_qualification_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.create_new_qualification()

    @allure.description("Test create shift")
    def test_create_shift(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = DirectoriesPage(browser, browser.current_url)
        page.open_shift_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.create_new_shift()

@allure.epic("Tests cancel create")
@pytest.mark.cancel
class TestCancelDirectories():

    @allure.description("Test cancel create object")
    def test_cancel_create_new_object(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_object_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.cancel_create_new_object()

    @allure.description("Test cancel create task")
    def test_cancel_create_new_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_task_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.cancel_create_new_task()

    @allure.description("Test cancel create qualification")
    def test_cancel_create_new_qualification(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_qualification_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.cancel_create_new_qualification()

    @allure.description("Test cancel create shift")
    def test_cancel_create_new_shift(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_shift_list()
        page = CreateDirectoriesPage(browser, browser.current_url)
        page.cancel_create_new_shift()

@allure.epic("Test edit function")
@pytest.mark.edit
class TestEditing():
    
    @allure.description("Test editing object")
    def test_editing_object(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_object_list()
        page.open_object_profile()
        page = EditDirectoriesPage(browser, browser.current_url)
        page.editing_object()


    @allure.description("Test editing task")
    def test_editing_task(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_task_list()
        page.open_task_profile()
        page = EditDirectoriesPage(browser, browser.current_url)
        page.editing_task()

    @allure.description("Test editing qualification")
    def test_editing_qualification(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_qualification_list()
        page.open_qualification_profile()
        page = EditDirectoriesPage(browser, browser.current_url)
        page.editing_qualification()

    @allure.description("Test editing shift")      
    def test_editing_shift(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.login_and_open_directories()
        page = DirectoriesPage(browser, browser.current_url)
        page.click_on_shift_list()
        page.open_shift_profile()
        page = EditDirectoriesPage(browser, browser.current_url)
        page.editing_shift()