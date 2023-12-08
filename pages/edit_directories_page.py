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

class EditDirectoriesPage(BasePage):

    def editing_object(self):
        with allure.step("Editing object"):
            f = open('pages/data/editing_data.json', encoding='utf-8')
            file_content = f.read()
            editing_data = json.loads(file_content)

            editing_button = self.browser.find_element(*DirectoriesPageLocators.EDITING_BUTTON).click()

            click_object_adress = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_ADRESS).click()
            select_object_adress = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_ADRESS).send_keys(Keys.CONTROL + "a")
            del_old_object_adress = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_ADRESS).send_keys(Keys.DELETE)

            editing_object_adress = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_ADRESS).send_keys(editing_data['object_adress'])

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.SAVE_EDITING_OBJECT_BUTTON)))
            save_editing_button = self.browser.find_element(*DirectoriesPageLocators.SAVE_EDITING_OBJECT_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном изменении объекта"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Данные успешно обновлены!", "Текст сообщения неверен"

            object_adress_data = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_ADRESS)
            object_adress_data_text = object_adress_data.get_attribute("value")
            assert object_adress_data_text == "г. Санкт-Петербург", "Данные не изменились"

    def editing_task(self):
        with allure.step("Editing task"):
            f = open('pages/data/editing_data.json', encoding='utf-8')
            file_content = f.read()
            editing_data = json.loads(file_content)

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.TASK_EDITING_BUTTON)))
            editing_button = self.browser.find_element(*DirectoriesPageLocators.TASK_EDITING_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.CREATE_TASK_NAME)))
            click_task_name = self.browser.find_element(*DirectoriesPageLocators.CREATE_TASK_NAME).click()
            select_task_names = self.browser.find_element(*DirectoriesPageLocators.CREATE_TASK_NAME).send_keys(Keys.CONTROL + "a")
            del_old_task_name = self.browser.find_element(*DirectoriesPageLocators.CREATE_TASK_NAME).send_keys(Keys.DELETE)

            editing_task_name = self.browser.find_element(*DirectoriesPageLocators.CREATE_TASK_NAME).send_keys(editing_data['task_name'])

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SAVE_EDITING_TASK_BUTTON)))
            save_task_button = self.browser.find_element(*DirectoriesPageLocators.SAVE_EDITING_TASK_BUTTON).click()
            
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном изменении типа задания"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Данные успешно обновлены!", "Текст сообщения неверен"

            task_name_data = self.browser.find_element(*DirectoriesPageLocators.CREATE_TASK_NAME)
            task_name_data_text = task_name_data.get_attribute("value")
            assert task_name_data_text == "Доп. смена", "Данные не изменились"

    def editing_qualification(self):
        with allure.step("Editing qualification"):
            f = open('pages/data/editing_data.json', encoding='utf-8')
            file_content = f.read()
            editing_data = json.loads(file_content)

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.QUALIFICATION_EDITING_BUTTON)))
            editing_button = self.browser.find_element(*DirectoriesPageLocators.QUALIFICATION_EDITING_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.CREATE_QUALIFICATION_PAYMENT)))
            click_task_name = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_PAYMENT).click()
            select_task_names = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_PAYMENT).send_keys(Keys.CONTROL + "a")
            del_old_task_name = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_PAYMENT).send_keys(Keys.DELETE)

            editing_task_name = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_PAYMENT).send_keys(editing_data['payment'])

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SAVE_EDITING_QUALIFICATION_BUTTON)))
            save_task_button = self.browser.find_element(*DirectoriesPageLocators.SAVE_EDITING_QUALIFICATION_BUTTON).click()
            
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном изменении специальности"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Данные успешно обновлены!", "Текст сообщения неверен"

            qualification_payment_data = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_PAYMENT)
            qualification_payment_data_text = qualification_payment_data.get_attribute("value")
            assert qualification_payment_data_text == "3000", "Данные не изменились"

    def editing_shift(self):
        with allure.step("Editing shift"):
            f = open('pages/data/editing_data.json', encoding='utf-8')
            file_content = f.read()
            editing_data = json.loads(file_content)

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SHIFT_EDITING_BUTTON)))
            editing_button = self.browser.find_element(*DirectoriesPageLocators.SHIFT_EDITING_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.ADD_SHIFT_NAME)))
            click_shift_name = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_NAME).click()
            select_shift_names = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_NAME).send_keys(Keys.CONTROL + "a")
            del_old_shift_name = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_NAME).send_keys(Keys.DELETE)

            editing_shift_name = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_NAME).send_keys(editing_data['shift_name'])

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.SAVE_EDITING_SHIFT_BUTTON)))
            save_shift_button = self.browser.find_element(*DirectoriesPageLocators.SAVE_EDITING_SHIFT_BUTTON).click()
            
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном изменении графика"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Данные успешно обновлены!", "Текст сообщения неверен"

            shift_name_data = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_NAME)
            shift_name_data_text = shift_name_data.get_attribute("value")
            assert shift_name_data_text == "Смена для теста", "Данные не изменились"

    