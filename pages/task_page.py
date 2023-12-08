from .base_page import BasePage
from .locators import ProfilePageLocators
from .locators import TaskPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import allure
import json
import time

class TaskPage(BasePage):

    def open_task_list(self):
        with allure.step("Open tasks list"):
            task_list_button = self.browser.find_element(*TaskPageLocators.TASKS_LIST).click()

    def open_task_profile(self):
        with allure.step("Open tasks profile"):
            task_profile = self.browser.find_element(*TaskPageLocators.TASK_PROFILE).click()

    def create_new_task(self):
        with allure.step("Create new task"):
            add_task_button = self.browser.find_element(*TaskPageLocators.ADD_TASK_BUTTON).click()

            type_task = self.browser.find_element(*TaskPageLocators.TYPE_TASK).click()
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((TaskPageLocators.SELECT_TYPE_TASK)))
            select_type_task = self.browser.find_element(*TaskPageLocators.SELECT_TYPE_TASK).click()

            task_description = self.browser.find_element(*TaskPageLocators.TASK_ADDITIONAL_DESCRIPTION).click()
            task_description = self.browser.find_element(*TaskPageLocators.TASK_ADDITIONAL_DESCRIPTION).send_keys("Дополнительное описание")

            number_of_employees = self.browser.find_element(*TaskPageLocators.NUMBER_OF_EMPLOYEES).send_keys(2)

            task_qualification = self.browser.find_element(*TaskPageLocators.TASK_QUALIFICATION).click()
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((TaskPageLocators.SELECT_TASK_QUALIFICATION)))
            select_type_qualification = self.browser.find_element(*TaskPageLocators.SELECT_TASK_QUALIFICATION).click()

            next_button = self.browser.find_element(*TaskPageLocators.NEXT_BUTTON).click()

            today_date = datetime.date.today().isoformat()
            task_date = today_date + str(datetime.timedelta(days=1))

            task_time = self.browser.find_element(*TaskPageLocators.TASK_DATE).send_keys(task_date)

            task_object = self.browser.find_element(*TaskPageLocators.TASK_OBJECT).click()
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((TaskPageLocators.SELECT_TASK_OBJECT)))
            select_type_task = self.browser.find_element(*TaskPageLocators.SELECT_TASK_OBJECT).click()

            save_task_button = self.browser.find_element(*TaskPageLocators.SAVE_TASK_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((TaskPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*TaskPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном создании сотрудника"
            success_message = self.browser.find_element(*TaskPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Задание успешно создано!", "Текст сообщения неверен"

    def editing_task(self):
        with allure.step("Editing task"):
            editing_task_button = self.browser.find_element(*TaskPageLocators.EDITING_TASK_BUTTON).click()

            click_number_of_employees = self.browser.find_element(*TaskPageLocators.NEW_NUMBER_OF_EMPLOYEES).click()
            select_number_of_employees = self.browser.find_element(*TaskPageLocators.NEW_NUMBER_OF_EMPLOYEES).send_keys(Keys.CONTROL + "a")
            del_old_number_of_employees = self.browser.find_element(*TaskPageLocators.NEW_NUMBER_OF_EMPLOYEES).send_keys(Keys.DELETE)
            number_of_employees = self.browser.find_element(*TaskPageLocators.NEW_NUMBER_OF_EMPLOYEES).send_keys(3)

            save_editing_task_button = self.browser.find_element(*TaskPageLocators.SAVE_EDITING_TASK_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((TaskPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*TaskPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном изменении графика"
            success_message = self.browser.find_element(*TaskPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Задание успешно обновлено!", "Текст сообщения неверен"

            number_of_employees_data = self.browser.find_element(*TaskPageLocators.NEW_NUMBER_OF_EMPLOYEES)
            number_of_employees_data_text = number_of_employees_data.get_attribute("value")
            assert number_of_employees_data_text == "3", "Данные не изменились"

    def delete_task(self):
        with allure.step("Delete task"):
            delete_task_button = self.browser.find_element(*TaskPageLocators.DELETE_TASK_BUTTON).click()

            assert self.is_element_present(*TaskPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном удалении графика"
            success_message = self.browser.find_element(*TaskPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Задание успешно удалено!", "Текст сообщения неверен"

            element = WebDriverWait(self.browser, 5).until(EC.invisibility_of_element_located((TaskPageLocators.SUCCESS_MESSAGE)))
            assert self.is_not_element_present(*TaskPageLocators.TASK_PROFILE), "Задание не удалено"  

    def cancel_create_new_task(self):
        with allure.step("Cancel create new task"):
            create_new_task = self.browser.find_element(*TaskPageLocators.ADD_TASK_BUTTON).click()

            cancel_create_task_button = self.browser.find_element(*TaskPageLocators.CANCEL_CREATE_BUTTON).click()
            time.sleep(1)

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/tasks/", "Не выполнился переход в список бригад"

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((TaskPageLocators.ADD_TASK_BUTTON)))
            create_new_shift = self.browser.find_element(*TaskPageLocators.ADD_TASK_BUTTON).click()

            cancel_arrow_create_shift_button = self.browser.find_element(*TaskPageLocators.CANCEL_ARROW_CREATE_BUTTON).click()
            time.sleep(1)

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/tasks", "Не выполнился переход в список бригад"

    def add_employees_to_task_and_replace(self):
        with allure.step("Add employees to task and replace"):
            
            f = open('pages/data/test_employees.json', encoding='utf-8')
            file_content = f.read()
            test_employees = json.loads(file_content)
            
            open_task_employee_list = self.browser.find_element(*TaskPageLocators.TASK_EMPLOYEE_LIST).click()
            add_task_employee = self.browser.find_element(*TaskPageLocators.ADD_TASK_EMPLOYEE).click()

            search_task_employee = self.browser.find_element(*TaskPageLocators.SEARCH_TASK_EMPLOYEE).send_keys(test_employees['personnel_numbers'][0])
            time.sleep(2)
            add_task_employees_button = self.browser.find_element(*TaskPageLocators.ADD_TASK_EMPLOYEE_BUTTON).click()

            replace_employee = self.browser.find_element(*TaskPageLocators.REPLACE_TASK_EMPLOYEE_BUTTON).click()

            search_task_employee = self.browser.find_element(*TaskPageLocators.SEARCH_TASK_EMPLOYEE).send_keys(test_employees['personnel_numbers'][1])
            time.sleep(2)
            add_task_employees_button = self.browser.find_element(*TaskPageLocators.ADD_TASK_EMPLOYEE_BUTTON).click()

    def create_empty_task(self):
        with allure.step("Create empty task"):
            add_task_button = self.browser.find_element(*TaskPageLocators.ADD_TASK_BUTTON).click()

            employee_number_message = self.browser.find_element(*TaskPageLocators.EMPLOYEES_NUMBER_MESSAGE)
            employee_number_message_text = employee_number_message.text
            assert employee_number_message_text == "Количество исполнителей не выбрано", "Неверное сообщение"

            assert self.element_is_not_clickable(*TaskPageLocators.NEXT_BUTTON), "Кнопка доступна для нажатия"