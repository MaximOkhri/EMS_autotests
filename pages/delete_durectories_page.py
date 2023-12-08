from .base_page import BasePage
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

class DeleteDirectoriesPage(BasePage):

    def delete_object(self):
        with allure.step("Delete object"):
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.DELETE_BUTTON)))
            delete_button = self.browser.find_element(*DirectoriesPageLocators.DELETE_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном удалении объекта"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Склад успешно удален!", "Текст сообщения неверен"

            element = WebDriverWait(self.browser, 5).until(EC.invisibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_not_element_present(By.XPATH, "//p[text()='Тестовый объект']"), "Объект не удален"

    def delete_task(self):
        with allure.step("Delete task"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.TASK_DELETE_BUTTON)))
            delete_button = self.browser.find_element(*DirectoriesPageLocators.TASK_DELETE_BUTTON).click()

            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном удалении типа задания"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Тип задания успешно удален!", "Текст сообщения неверен"

            element = WebDriverWait(self.browser, 5).until(EC.invisibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_not_element_present(*DirectoriesPageLocators.OPEN_TASK_PROFILE), "Тип задания не удален"

    def delete_qualification(self):
        with allure.step("Delete qualification"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.QUALIFICATION_DELETE_BUTTON)))
            delete_button = self.browser.find_element(*DirectoriesPageLocators.QUALIFICATION_DELETE_BUTTON).click()

            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном удалении специальности"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Специальность успешно удалена!", "Текст сообщения неверен"

            element = WebDriverWait(self.browser, 5).until(EC.invisibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_not_element_present(*DirectoriesPageLocators.OPEN_QUALIFICATION_PROFILE), "Специальность не удалена"

    def delete_shift(self):
        with allure.step("Delete shift"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SHIFT_DELETE_BUTTON)))
            delete_button = self.browser.find_element(*DirectoriesPageLocators.SHIFT_DELETE_BUTTON).click()

            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном удалении графика"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "График успешно удален!", "Текст сообщения неверен"

            element = WebDriverWait(self.browser, 5).until(EC.invisibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_not_element_present(*DirectoriesPageLocators.OPEN_SHIFT_PROFILE), "График не удален"