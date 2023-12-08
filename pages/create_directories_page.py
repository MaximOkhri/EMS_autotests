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

class CreateDirectoriesPage(BasePage):
    
    def create_new_object(self):
        with allure.step("Create new object"):
            f = open('pages/data/object_data.json', encoding='utf-8')
            file_content = f.read()
            object_data = json.loads(file_content)

            create_new_object = self.browser.find_element(*DirectoriesPageLocators.ADD_OBJECT_BUTTON).click()
            name_object = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_NAME).send_keys(object_data['name'])
            adress_object = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_ADRESS).send_keys(object_data['adress'])
            object_contact_person = self.browser.find_element(*DirectoriesPageLocators.CREATE_CONTACT_PERSON).click()
            
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SELECT_CONTACT_PERSON)))
            select_contact_person = self.browser.find_element(*DirectoriesPageLocators.SELECT_CONTACT_PERSON).click()

            object_phone = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_PHONE).click()
            object_phone = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_PHONE).send_keys(object_data['phone'])
            object_email = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_EMAIL).send_keys(object_data['email'])
            shift_name = self.browser.find_element(*DirectoriesPageLocators.CREATE_SHIFT_NAME).send_keys(object_data['shift_name'])
            short_name = self.browser.find_element(*DirectoriesPageLocators.CREATE_SHORT_NAME).send_keys(object_data['short_shift_name'])
            start_shift = self.browser.find_element(*DirectoriesPageLocators.CREATE_START_SHIFT).send_keys(object_data['shift_start'])
            ok_start_shift = self.browser.find_element(*DirectoriesPageLocators.OK_START_SHIFT).click()
            end_shift = self.browser.find_element(*DirectoriesPageLocators.CREATE_END_SHIFT).send_keys(object_data['shift_end'])
            ok_end_shift = self.browser.find_element(*DirectoriesPageLocators.OK_END_SHIFT).click()
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.CREATE_OBJECT_BUTTON)))
            create_object_button = self.browser.find_element(*DirectoriesPageLocators.CREATE_OBJECT_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном создании объекта"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Объект успешно сохранен!", "Текст сообщения неверен"

    def create_new_type_task(self):
        with allure.step("Create new task"):
            f = open('pages/data/task_data.json', encoding='utf-8')
            file_content = f.read()
            task_data = json.loads(file_content)

            create_new_task = self.browser.find_element(*DirectoriesPageLocators.ADD_TASK_BUTTON).click()
            name_task = self.browser.find_element(*DirectoriesPageLocators.CREATE_TASK_NAME).send_keys(task_data['name'])

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.CREATE_TASK_DESCRIPTION)))
            click_description_task = self.browser.find_element(*DirectoriesPageLocators.CREATE_TASK_DESCRIPTION).click()
            description_task = self.browser.find_element(*DirectoriesPageLocators.CREATE_TASK_DESCRIPTION).send_keys(task_data['description'])
            
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.CREATE_TASK_BUTTON)))
            create_task_button = self.browser.find_element(*DirectoriesPageLocators.CREATE_TASK_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.OPEN_TASK_PROFILE)))

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном создании типа задания"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Задание успешно сохранено!", "Текст сообщения неверен"

    def create_new_qualification(self):
        with allure.step("Create new qualification"):
            f = open('pages/data/qalification_data.json', encoding='utf-8')
            file_content = f.read()
            qalification_data = json.loads(file_content)

            create_new_qualification = self.browser.find_element(*DirectoriesPageLocators.ADD_QUALIFICATION_BUTTON).click()
            name_qualification = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_NAME).send_keys(qalification_data['name'])
            payment_qualification = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_PAYMENT).send_keys(qalification_data['payment'])

            qualification_payment_rate = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_PAYMENT_RATE).click()
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SELECT_QUALIFICATION_PAYMENT_RATE)))
            select_qualification_payment_rate = self.browser.find_element(*DirectoriesPageLocators.SELECT_QUALIFICATION_PAYMENT_RATE).click()

            plan_count = self.browser.find_element(*DirectoriesPageLocators.PLAN_COUNT).send_keys(qalification_data['employee_number'])
            
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.CREATE_QUALIFICATION_BUTTON)))
            create_qualification_button = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном создании специальности"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "Новая специальность успешно создана!", "Текст сообщения неверен"

    def create_new_shift(self):
        with allure.step("Create new shift"):
            f = open('pages/data/shift_data.json', encoding='utf-8')
            file_content = f.read()
            shift_data = json.loads(file_content)

            create_new_shift = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_BUTTON).click()

            name_shift = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_NAME).send_keys(shift_data['name'])
            description_shift = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_DESCRIPTION).send_keys(shift_data['description'])

            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((DirectoriesPageLocators.FINALLY_CREATE_SHIFT_BUTTON)))
            create_shift_button = self.browser.find_element(*DirectoriesPageLocators.FINALLY_CREATE_SHIFT_BUTTON).click()

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.OPEN_SHIFT_PROFILE)))

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.SUCCESS_MESSAGE)))
            assert self.is_element_present(*DirectoriesPageLocators.SUCCESS_MESSAGE), "Отсутствует сообщение об успешном создании графика"
            success_message = self.browser.find_element(*DirectoriesPageLocators.SUCCESS_MESSAGE)
            success_message_text = success_message.text
            assert success_message_text == "График успешно сохранен!", "Текст сообщения неверен"

    def cancel_create_new_object(self):
        with allure.step("Cancel create object"):
            create_new_object = self.browser.find_element(*DirectoriesPageLocators.ADD_OBJECT_BUTTON).click()

            cancel_create_shift_button = self.browser.find_element(*DirectoriesPageLocators.CANCEL_OBJECT_BUTTON).click()

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/workplacesList", "Не выполнился переход в список объектов"

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.ADD_OBJECT_BUTTON)))
            create_new_shift = self.browser.find_element(*DirectoriesPageLocators.ADD_OBJECT_BUTTON).click()

            cancel_arrow_create_shift_button = self.browser.find_element(*DirectoriesPageLocators.CANCEL_ARROW_OBJECT_BUTTON).click()

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/workplacesList", "Не выполнился переход в список объектов"

    def cancel_create_new_task(self):
        with allure.step("Cancel create task"):
            create_new_task = self.browser.find_element(*DirectoriesPageLocators.ADD_TASK_BUTTON).click()

            cancel_create_shift_button = self.browser.find_element(*DirectoriesPageLocators.CANCEL_TASK_BUTTON).click()

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/dirTasksList", "Не выполнился переход в список типов задания"

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.ADD_TASK_BUTTON)))
            create_new_shift = self.browser.find_element(*DirectoriesPageLocators.ADD_TASK_BUTTON).click()

            cancel_arrow_create_shift_button = self.browser.find_element(*DirectoriesPageLocators.CANCEL_ARROW_TASK_BUTTON).click()

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/dirTasksList", "Не выполнился переход в список типов задания"

    def cancel_create_new_qualification(self):
        with allure.step("Cancel create qualification"):
            create_new_qualification = self.browser.find_element(*DirectoriesPageLocators.ADD_QUALIFICATION_BUTTON).click()

            cancel_create_shift_button = self.browser.find_element(*DirectoriesPageLocators.CANCEL_QUALIFICATION_BUTTON).click()
            time.sleep(1)

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/dirQualificationslist", "Не выполнился переход в список специальностей"

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.ADD_QUALIFICATION_BUTTON)))
            create_new_shift = self.browser.find_element(*DirectoriesPageLocators.ADD_QUALIFICATION_BUTTON).click()

            cancel_arrow_create_shift_button = self.browser.find_element(*DirectoriesPageLocators.CANCEL_ARROW_QUALIFICATION_BUTTON).click()
            time.sleep(1)

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/dirQualificationslist", "Не выполнился переход в список специальностей"

    def cancel_create_new_shift(self):
        with allure.step("Cancel create shift"):
            create_new_shift = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_BUTTON).click()

            cancel_create_shift_button = self.browser.find_element(*DirectoriesPageLocators.CANCEL_SHIFT_BUTTON).click()

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/scheduleTypes", "Не выполнился переход в список графиков"

            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((DirectoriesPageLocators.ADD_SHIFT_BUTTON)))
            create_new_shift = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_BUTTON).click()

            cancel_arrow_create_shift_button = self.browser.find_element(*DirectoriesPageLocators.CANCEL_ARROW_SHIFT_BUTTON).click()

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/scheduleTypes", "Не выполнился переход в список графиков"

    def create_empty_object(self):
        with allure.step("Create empty object"):
            add_new_object = self.browser.find_element(*DirectoriesPageLocators.ADD_OBJECT_BUTTON).click()

            object_name_message = self.browser.find_element(*DirectoriesPageLocators.OBJECT_NAME_MESSAGE)
            object_name_message_text = object_name_message.text
            assert object_name_message_text == "Укажите название объекта", "Неверное сообщение"

            adress_message = self.browser.find_element(*DirectoriesPageLocators.ADDRESS_MESSAGE)
            adress_message_text = adress_message.text
            assert adress_message_text == "Укажите адрес объекта", "Неверное сообщение"

            assert self.element_is_not_clickable(*DirectoriesPageLocators.CREATE_OBJECT_BUTTON), "Кнопка доступна для нажатия" 

    def create_empty_task(self):
        with allure.step("Create empty task"):
            add_task_button = self.browser.find_element(*DirectoriesPageLocators.ADD_TASK_BUTTON).click()

            name_message = self.browser.find_element(*DirectoriesPageLocators.NAME_MESSAGE)
            name_message_text = name_message.text
            assert name_message_text == "Укажите наименование", "Неверное сообщение"

            description_message = self.browser.find_element(*DirectoriesPageLocators.DESCRIPTION_MESSAGE)
            description_message_text = description_message.text
            assert description_message_text == "Добавьте описание", "Неверное сообщение"

            assert self.element_is_not_clickable(*DirectoriesPageLocators.CREATE_TASK_BUTTON), "Кнопка доступна для нажатия"

    def create_empty_qualification(self):
        with allure.step("Create empty qualification"):
            add_qualification_button = self.browser.find_element(*DirectoriesPageLocators.ADD_QUALIFICATION_BUTTON).click()

            click_save_button = self.browser.find_element(*DirectoriesPageLocators.CREATE_QUALIFICATION_BUTTON).click()

            get_url = self.browser.current_url
            assert str(get_url) == "https://ems.biacorp.ru/dirQualificationslist/newDirQualification", "Выполнился переход на другую страницу"

        
    def create_empty_shift(self):
        with allure.step("Create empty shift"):
            add_shift_button = self.browser.find_element(*DirectoriesPageLocators.ADD_SHIFT_BUTTON).click()

            shift_name_message = self.browser.find_element(*DirectoriesPageLocators.SHIFT_NAME_MESSAGE)
            shift_name_message_text = shift_name_message.text
            assert shift_name_message_text == "Введите название графика", "Неверное сообщение"

            assert self.element_is_not_clickable(*DirectoriesPageLocators.FINALLY_CREATE_SHIFT_BUTTON), "Кнопка доступна для нажатия"