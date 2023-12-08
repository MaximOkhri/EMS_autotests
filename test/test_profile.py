from EMS_autotests.pages.base_page import BasePage
from EMS_autotests.pages.profile_page import ProfilePage
from EMS_autotests.pages.locators import MainLink
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
import allure

@allure.epic("Test profile")
@pytest.mark.profile
class TestProfile():
    
    @allure.description("Editing profile data")
    def test_editing_profile(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = ProfilePage(browser, browser.current_url)
        page.open_profile_information()
        page.editing_profile_data()

    @allure.description("Save settings without editing")
    def test_save_settings_without_editing(self, browser: WebDriver):
        page = BasePage(browser, MainLink.LINK)
        page.open()
        page.open_login_window_and_write_user_data()
        page = ProfilePage(browser, browser.current_url)
        page.open_profile_information()
        page.save_profile_without_editing()