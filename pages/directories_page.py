from .base_page import BasePage
from .locators import MainLink
from .locators import ProfilePageLocators
from .locators import DirectoriesPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import json
import time

class DirectoriesPage(BasePage):

    def open_object_list(self):
        with allure.step("Open object list"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((ProfilePageLocators.USER_ICON_DROPDOWN)))
            user_dropdown = self.browser.find_element(*ProfilePageLocators.USER_ICON_DROPDOWN).click()
            
            dropdown_directories_list = self.browser.find_element(*DirectoriesPageLocators.DROPDOWN_DIRECTORIES_LIST).click()
            
            open_object_list = self.browser.find_element(*DirectoriesPageLocators.OBJECT_LIST).click()

    def open_tasks_list(self):
        with allure.step("Open tasks list"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((ProfilePageLocators.USER_ICON_DROPDOWN)))
            user_dropdown = self.browser.find_element(*ProfilePageLocators.USER_ICON_DROPDOWN).click()
            
            dropdown_directories_list = self.browser.find_element(*DirectoriesPageLocators.DROPDOWN_DIRECTORIES_LIST).click()
            
            open_task_list = self.browser.find_element(*DirectoriesPageLocators.TASK_LIST).click()

    def open_qualification_list(self):
        with allure.step("Open qualification list"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((ProfilePageLocators.USER_ICON_DROPDOWN)))
            user_dropdown = self.browser.find_element(*ProfilePageLocators.USER_ICON_DROPDOWN).click()
            
            dropdown_directories_list = self.browser.find_element(*DirectoriesPageLocators.DROPDOWN_DIRECTORIES_LIST).click()
            
            open_qualification_list = self.browser.find_element(*DirectoriesPageLocators.QUALIFICATION_LIST).click()

    def open_shift_list(self):
        with allure.step("Open shift list"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((ProfilePageLocators.USER_ICON_DROPDOWN)))
            user_dropdown = self.browser.find_element(*ProfilePageLocators.USER_ICON_DROPDOWN).click()
            
            dropdown_directories_list = self.browser.find_element(*DirectoriesPageLocators.DROPDOWN_DIRECTORIES_LIST).click()
            
            open_shift_list = self.browser.find_element(*DirectoriesPageLocators.SHIFT_LIST).click()

    def open_object_profile(self):
        with allure.step("Open object profile"):
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.OPEN_OBJECT_PROFILE)))
            test_object = self.browser.find_element(*DirectoriesPageLocators.OPEN_OBJECT_PROFILE).click()

    def open_task_profile(self):
        with allure.step("Open task profile"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.OPEN_TASK_PROFILE)))
            test_task = self.browser.find_element(*DirectoriesPageLocators.OPEN_TASK_PROFILE).click() 

    def open_qualification_profile(self):
        with allure.step("Open qualification profile"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.OPEN_QUALIFICATION_PROFILE)))
            test_qualification = self.browser.find_element(*DirectoriesPageLocators.OPEN_QUALIFICATION_PROFILE).click()

    def open_shift_profile(self):
        with allure.step("Open shift profile"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.OPEN_SHIFT_PROFILE)))
            test_qualification = self.browser.find_element(*DirectoriesPageLocators.OPEN_SHIFT_PROFILE).click()
    
    def click_on_object_list(self):
        with allure.step("Click on objects list"):
            click_on_object_list = self.browser.find_element(*DirectoriesPageLocators.OBJECT_LIST).click()
            time.sleep(2)

    def click_on_task_list(self):
        with allure.step("Click on tasks list"):
            click_on_object_list = self.browser.find_element(*DirectoriesPageLocators.TASK_LIST).click()
            time.sleep(2)

    def click_on_qualification_list(self):
        with allure.step("Click on qualifications list"):
            click_on_object_list = self.browser.find_element(*DirectoriesPageLocators.QUALIFICATION_LIST).click()
            time.sleep(2)

    def click_on_shift_list(self):
        with allure.step("Click on shift list"):
            click_on_object_list = self.browser.find_element(*DirectoriesPageLocators.SHIFT_LIST).click()
            time.sleep(2)