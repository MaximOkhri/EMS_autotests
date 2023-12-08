from .base_page import BasePage
from .locators import BrigadesPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import json
import time

class BrigadesPage(BasePage):

    def open_brigades_list(self):
        with allure.step("Open brigades list"):
            brigades_list_button = self.browser.find_element(*BrigadesPageLocators.BRIGADES_LIST).click()        

    def open_brigade_profile(self):
        with allure.step("Open brigade profile"):
            brigade_profile_button = self.browser.find_element(*BrigadesPageLocators.BRIGADES_PROFILE).click()
    
    def create_new_brigade(self):
        with allure.step("Create new brigade"):
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.CREATE_BRIGADE_BUTTON)))
            create_brigade_button = self.browser.find_element(*BrigadesPageLocators.CREATE_BRIGADE_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((BrigadesPageLocators.BRIGADE_NAME)))
            brigade_name = self.browser.find_element(*BrigadesPageLocators.BRIGADE_NAME).send_keys("Тестовая бригада")
            
            brigade_brigadier_menu = self.browser.find_element(*BrigadesPageLocators.BRIGADE_BRIGADIER).click()
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((BrigadesPageLocators.BRIGADE_BRIGADIER)))
            select_brigadier = self.browser.find_element(*BrigadesPageLocators.SELECT_BRIGADE_BRIGADIER).click()

            object_brigade_menu = self.browser.find_element(*BrigadesPageLocators.BRIGADE_OBJECT).click()
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((BrigadesPageLocators.BRIGADE_OBJECT)))
            select_object = self.browser.find_element(*BrigadesPageLocators.SELECT_BRIGADE_OBJECT).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.NEXT_BUTTON)))
            next_button = self.browser.find_element(*BrigadesPageLocators.NEXT_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.ADD_EMPLOYEES_MENU)))
            add_employees_menu = self.browser.find_element(*BrigadesPageLocators.ADD_EMPLOYEES_MENU).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.ADD_EMPLOYEE)))
            add_employee = self.browser.find_element(*BrigadesPageLocators.ADD_EMPLOYEE).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.SAVE_BUTTON)))
            save_button = self.browser.find_element(*BrigadesPageLocators.SAVE_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*BrigadesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном создании бригады"
            success_message = self.browser.find_element(*BrigadesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Бригада успешно создана!", "Текст сообщения неверен"

    def editing_brigade(self):
        with allure.step("Editing brigade"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((BrigadesPageLocators.EDITING_BUTTON)))
            editing_button = self.browser.find_element(*BrigadesPageLocators.EDITING_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.BRIGADE_NAME)))
            click_brigade_name = self.browser.find_element(*BrigadesPageLocators.BRIGADE_NAME).click()
            select_brigade_name = self.browser.find_element(*BrigadesPageLocators.BRIGADE_NAME).send_keys(Keys.CONTROL + "a")
            delete_old_brigade_name = self.browser.find_element(*BrigadesPageLocators.BRIGADE_NAME).send_keys(Keys.DELETE)

            editing_brigade_name = self.browser.find_element(*BrigadesPageLocators.BRIGADE_NAME).send_keys("Бригада для теста")

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.SAVE_EDITING_BUTTON)))
            save_brigade_button = self.browser.find_element(*BrigadesPageLocators.SAVE_EDITING_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((BrigadesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*BrigadesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном изменении бригады"
            success_message = self.browser.find_element(*BrigadesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Данные успешно обновлены!", "Текст сообщения неверен"

            brigade_name_data = self.browser.find_element(*BrigadesPageLocators.BRIGADE_NAME)
            brigade_name_data_text = brigade_name_data.get_attribute("value")
            assert brigade_name_data_text == "Бригада для теста", "Данные не изменились"

    def delete_brigade(self):
        with allure.step("Delete brigade"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((BrigadesPageLocators.DELETE_BUTTON)))
            delete_button = self.browser.find_element(*BrigadesPageLocators.DELETE_BUTTON).click() 

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((BrigadesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*BrigadesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном удалении бригады"
            success_message = self.browser.find_element(*BrigadesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Бригада успешно удалена!", "Текст сообщения неверен"

            element = WebDriverWait(self.browser, 5).until(EC.invisibility_of_element_located((BrigadesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_not_element_present(By.XPATH, "//div[text()='Петров Николай']"), "Бригада не удалена"

    def cancel_create_new_brigade(self):
        with allure.step("Cancel create brigade"):
            create_new_brigade = self.browser.find_element(*BrigadesPageLocators.CREATE_BRIGADE_BUTTON).click()

            cancel_create_brigade_button = self.browser.find_element(*BrigadesPageLocators.CANCEL_BRIGADE_BUTTON).click()
            time.sleep(1)

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/brigades/", "Не выполнился переход в список бригад"

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((BrigadesPageLocators.CREATE_BRIGADE_BUTTON)))
            create_new_shift = self.browser.find_element(*BrigadesPageLocators.CREATE_BRIGADE_BUTTON).click()

            cancel_arrow_create_shift_button = self.browser.find_element(*BrigadesPageLocators.CANCEL_ARROW_BRIGADE_BUTTON).click()
            time.sleep(1)

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/brigades", "Не выполнился переход в список бригад"

    def add_employees_in_brigade(self):
        with allure.step("Add employees in brigade"):

            f = open('pages/data/test_employees.json', encoding='utf-8')
            file_content = f.read()
            test_employees = json.loads(file_content)

            brigade_employees = self.browser.find_element(*BrigadesPageLocators.BRIGADE_EMPLOYEES).click()

            add_brigade_employees = self.browser.find_element(*BrigadesPageLocators.ADD_BRIGADE_EMPLOYEES).click()
            search_brigade_employee = self.browser.find_element(*BrigadesPageLocators.SEARCH_BRIGADE_EMPLOYEE).send_keys(test_employees['personnel_numbers'][0])
            time.sleep(2)
            add_brigade_employees_button = self.browser.find_element(*BrigadesPageLocators.ADD_BRIGADE_EMPLOYEES_BUTTON).click()

            add_brigade_employees = self.browser.find_element(*BrigadesPageLocators.ADD_BRIGADE_EMPLOYEES).click()
            search_brigade_employee = self.browser.find_element(*BrigadesPageLocators.SEARCH_BRIGADE_EMPLOYEE).send_keys(test_employees['personnel_numbers'][1])
            time.sleep(2)
            add_brigade_employees_button = self.browser.find_element(*BrigadesPageLocators.ADD_BRIGADE_EMPLOYEES_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*BrigadesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном создании бригады"
            success_message = self.browser.find_element(*BrigadesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Сотрудник успешно добавлен!", "Текст сообщения неверен"

    def delete_employees_from_brigade(self):
        with allure.step("Delete employees from brigade"):
            brigade_employees = self.browser.find_element(*BrigadesPageLocators.BRIGADE_EMPLOYEES).click()

            delete_employee_button = self.browser.find_element(*BrigadesPageLocators.DELETE_EMPLOYEE_BUTTON).click()
            time.sleep(1)
            delete_employee_button = self.browser.find_element(*BrigadesPageLocators.DELETE_EMPLOYEE_BUTTON).click()
            time.sleep(1)

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((BrigadesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*BrigadesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном создании бригады"
            success_message = self.browser.find_element(*BrigadesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Сотрудник успешно удален!", "Текст сообщения неверен"

    def create_empty_brigade(self):
        with allure.step("Create empty brigade"):
            create_brigade_button = self.browser.find_element(*BrigadesPageLocators.CREATE_BRIGADE_BUTTON).click()

            assert self.element_is_not_clickable(*BrigadesPageLocators.NEXT_BUTTON), "Кнопка доступна для нажатия"