from .base_page import BasePage
from .locators import EmployeesPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import json
import time

class EmployeePage(BasePage):

    def open_employee_list(self):
        with allure.step("Open employee list"):
            employees_list_button = self.browser.find_element(*EmployeesPageLocators.EMPLOYEES_LIST_BUTTON).click()

    def open_employee_profile(self):
        with allure.step("Open employee profile"):
            employee_profile = self.browser.find_element(*EmployeesPageLocators.EMPLOYEE_PROFILE).click()

    def create_new_employee(self):
        with allure.step("Create new employee"):
            f = open('pages/data/employee_data.json', encoding='utf-8')
            file_content = f.read()
            employee_data = json.loads(file_content)

            create_employee_button = self.browser.find_element(*EmployeesPageLocators.CREATE_EMPLOYEE_BUTTON).click()

            add_manually = self.browser.find_element(*EmployeesPageLocators.ADD_MANUALLY).click()

            surname = self.browser.find_element(*EmployeesPageLocators.FIRST_NAME).send_keys(employee_data['first_name'])
            name = self.browser.find_element(*EmployeesPageLocators.LAST_NAME).send_keys(employee_data['last_name'])
            personnel_number = self.browser.find_element(*EmployeesPageLocators.PERSONNEL_NUMBER).send_keys(employee_data['personnel_number'])
            
            phone = self.browser.find_element(*EmployeesPageLocators.PHONE_NUMBER).click()
            phone = self.browser.find_element(*EmployeesPageLocators.PHONE_NUMBER).send_keys(employee_data['phone'])

            shift = self.browser.find_element(*EmployeesPageLocators.SHIFT).click()
            select_shift = self.browser.find_element(*EmployeesPageLocators.SELECT_SHIFT).click()

            shift_start = self.browser.find_element(*EmployeesPageLocators.SHIFT_START).send_keys(employee_data['shift_start'])
            ok_shift_start = self.browser.find_element(*EmployeesPageLocators.OK_SHIFT_START).click()
            shift_end = self.browser.find_element(*EmployeesPageLocators.SHIFT_END).send_keys(employee_data['shift_end'])
            ok_shift_end = self.browser.find_element(*EmployeesPageLocators.OK_SHIFT_END).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((EmployeesPageLocators.FINALLY_CREATE_BUTTON)))
            finally_create_button = self.browser.find_element(*EmployeesPageLocators.FINALLY_CREATE_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((EmployeesPageLocators.EMPLOYEE_PROFILE)))
            assert self.is_element_present(*EmployeesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном создании сотрудника"
            success_message = self.browser.find_element(*EmployeesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Сотрудник успешно создан!", "Текст сообщения неверен"

    def editing_employee(self):
        with allure.step("Editing employee"):
            f = open('pages/data/editing_data.json', encoding='utf-8')
            file_content = f.read()
            editing_data = json.loads(file_content)

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((EmployeesPageLocators.EDITING_BUTTON)))
            editing_button = self.browser.find_element(*EmployeesPageLocators.EDITING_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((EmployeesPageLocators.LAST_NAME)))
            click_employee_name = self.browser.find_element(*EmployeesPageLocators.LAST_NAME).click()
            select_employee_name = self.browser.find_element(*EmployeesPageLocators.LAST_NAME).send_keys(Keys.CONTROL + "a")
            delete_old_employee_name = self.browser.find_element(*EmployeesPageLocators.LAST_NAME).send_keys(Keys.DELETE)

            editing_employee_name = self.browser.find_element(*EmployeesPageLocators.LAST_NAME).send_keys(editing_data['employee_last_name'])

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((EmployeesPageLocators.EDITING_SAVE_BUTTON)))
            save_employee_button = self.browser.find_element(*EmployeesPageLocators.EDITING_SAVE_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((EmployeesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*EmployeesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном изменении сотрудника"
            success_message = self.browser.find_element(*EmployeesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Данные успешно обновлены!", "Текст сообщения неверен"

            employee_name_data = self.browser.find_element(*EmployeesPageLocators.LAST_NAME)
            employee_name_data_text = employee_name_data.get_attribute("value")
            assert employee_name_data_text == "Николай", "Данные не изменились"

    def delete_employee(self):
        with allure.step("Delete employee"):
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((EmployeesPageLocators.DELETE_BUTTON)))
            delete_button = self.browser.find_element(*EmployeesPageLocators.DELETE_BUTTON).click() 

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((EmployeesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*EmployeesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном удалении сотрудника"
            success_message = self.browser.find_element(*EmployeesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Сотрудник успешно удален!", "Текст сообщения неверен"

            element = WebDriverWait(self.browser, 5).until(EC.invisibility_of_element_located((EmployeesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_not_element_present(By.XPATH, "//p[text()='Петров Николай']"), "Объект не удален" 

    def cancel_create_new_employee(self):
        with allure.step("Cancel create employee"):
            create_new_employee = self.browser.find_element(*EmployeesPageLocators.CREATE_EMPLOYEE_BUTTON).click()

            add_manually = self.browser.find_element(*EmployeesPageLocators.ADD_MANUALLY).click()

            cancel_create_employee_button = self.browser.find_element(*EmployeesPageLocators.CANCEL_EMPLOYEE_BUTTON).click()

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/employees", "Не выполнился переход в список сотрудников"

    def cancel_choice_of_method_add_manually(self):
        with allure.step("Cancel add manually"):
            add_employee_button = self.browser.find_element(*EmployeesPageLocators.CREATE_EMPLOYEE_BUTTON).click()

            cancel_add_manually = self.browser.find_element(*EmployeesPageLocators.CANCEL_ADD_MANUALLY).click()

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/employees", "Не выполнился переход в список сотрудников"

    def create_empty_employee(self):
        with allure.step("Create empty emplpyee"):
            create_employee_button = self.browser.find_element(*EmployeesPageLocators.CREATE_EMPLOYEE_BUTTON).click()

            add_manually = self.browser.find_element(*EmployeesPageLocators.ADD_MANUALLY).click()

            employee_first_name_message = self.browser.find_element(*EmployeesPageLocators.FIRST_NAME_MESSAGE)
            employee_first_name_message_text = employee_first_name_message.text
            assert employee_first_name_message_text == "Укажите фамилию сотрудника", "Неверное сообщение"

            employee_last_name_message = self.browser.find_element(*EmployeesPageLocators.LAST_NAME_MESSAGE)
            employee_last_name_message_text = employee_last_name_message.text
            assert employee_last_name_message_text == "Укажите имя сотрудника", "Неверное сообщение"

            employee_personnel_number_message = self.browser.find_element(*EmployeesPageLocators.PERSONNEL_NUMBER_MESSAGE)
            employee_personnel_number_message_text = employee_personnel_number_message.text
            assert employee_personnel_number_message_text == "Укажите табельный номер", "Неверное сообщение"

            assert self.element_is_not_clickable(*EmployeesPageLocators.FINALLY_CREATE_BUTTON), "Кнопка доступна для нажатия"