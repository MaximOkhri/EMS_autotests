from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from .locators import MainLink
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import EmployeesPageLocators
from random import choices
import string
import allure
import json
import time

class BasePage():
    def __init__(self, browser: WebDriver, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        with allure.step("Open browser"):
            self.browser.get(self.url)
            self.browser.maximize_window()
        
    def open_registration_window(self):
        registration_window_button = self.browser.find_element(*MainPageLocators.registration_button)
        registration_window_button.click()

    def open_login_window_and_write_user_data(self):
        with allure.step("Login user"):
            login_window_button = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
            login_window_button.click()
            
            f = open('pages/data/user_data.json', encoding='utf-8')
            file_content = f.read()
            user_data = json.loads(file_content)

            e_mail = self.browser.find_element(*LoginPageLocators.E_MAIL)
            e_mail.send_keys(user_data['email'])
            user_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
            user_password.send_keys(user_data['user_password'])
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((LoginPageLocators.LOGIN_USER)))
            login_button = self.browser.find_element(*LoginPageLocators.LOGIN_USER)
            login_button.click()

    def login_and_open_directories(self):
        with allure.step("Login user and open discription"):
            login_window_button = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
            login_window_button.click()
            
            f = open('pages/data/user_data.json', encoding='utf-8')
            file_content = f.read()
            user_data = json.loads(file_content)

            e_mail = self.browser.find_element(*LoginPageLocators.E_MAIL)
            e_mail.send_keys(user_data['email'])
            user_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
            user_password.send_keys(user_data['user_password'])
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((LoginPageLocators.LOGIN_USER)))
            login_button = self.browser.find_element(*LoginPageLocators.LOGIN_USER)
            login_button.click()
            time.sleep(1)

            cookies = self.browser.get_cookies()

            for cookie in cookies:
                self.browser.add_cookie(cookie)

            self.browser.get(MainLink.DIRECTORIES_LINK)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return True
        return False

    def element_is_not_clickable(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except(ElementClickInterceptedException):
            return True
        return False

    def create_test_employees(self):
        with allure.step("Create employees for test"):
            i = 0
            f = open('pages/data/test_employees.json', 'a', encoding='utf-8')
            f.write("{\n")
            f.write('\t"personnel_numbers": [\n')
            while (i < 2):
                create_new_employee = self.browser.find_element(*EmployeesPageLocators.CREATE_EMPLOYEE_BUTTON).click()

                add_manually = self.browser.find_element(*EmployeesPageLocators.ADD_MANUALLY).click()

                first_name = ''.join(choices(string.ascii_lowercase, k=10))
                add_first_name = self.browser.find_element(*EmployeesPageLocators.FIRST_NAME).send_keys(first_name)
                last_name = ''.join(choices(string.ascii_lowercase, k=10))
                add_last_name = self.browser.find_element(*EmployeesPageLocators.LAST_NAME).send_keys(last_name)
                personel_number = ''.join(choices(string.digits, k=6))
                add_personnel_number = self.browser.find_element(*EmployeesPageLocators.PERSONNEL_NUMBER).send_keys(personel_number)

                phone_number = ''.join(choices(string.digits, k=10))
                while (phone_number[0] == '0'):
                    phone_number = ''.join(choices(string.digits, k=10))

                click_phone_number = self.browser.find_element(*EmployeesPageLocators.PHONE_NUMBER).click()
                add_phone_number = self.browser.find_element(*EmployeesPageLocators.PHONE_NUMBER).send_keys(phone_number)

                # shift = self.browser.find_element(*EmployeesPageLocators.SHIFT).click()
                # select_shift = self.browser.find_element(*EmployeesPageLocators.SELECT_SHIFT).click()

                # shift_start = self.browser.find_element(*EmployeesPageLocators.SHIFT_START).send_keys("08:00")
                # ok_shift_start = self.browser.find_element(*EmployeesPageLocators.OK_SHIFT_START).click()
                # shift_end = self.browser.find_element(*EmployeesPageLocators.SHIFT_END).send_keys("20:00")
                # ok_shift_end = self.browser.find_element(*EmployeesPageLocators.OK_SHIFT_END).click()

                element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((EmployeesPageLocators.FINALLY_CREATE_BUTTON)))
                finally_create_button = self.browser.find_element(*EmployeesPageLocators.FINALLY_CREATE_BUTTON).click()

                if (i < 1):
                    f.write('\t"' + personel_number + '",\n')
                else:
                    f.write('\t"' + personel_number + '"\n')

                time.sleep(1)
                i = i + 1
            f.write('\t]\n')
            f.write("}\n")

    def delete_test_employees(self):
        with allure.step("Delete test employee"):
            i = 0
            while (i < 2):
                f = open('pages/data/test_employees.json', encoding='utf-8')
                file_content = f.read()
                test_employees = json.loads(file_content)
                time.sleep(2)

                employee_profile = self.browser.find_element(By.XPATH, "//p[text()= '"+ test_employees['personnel_numbers'][i] +"']").click()

                i = i + 1

                element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((EmployeesPageLocators.DELETE_BUTTON)))
                delete_button = self.browser.find_element(*EmployeesPageLocators.DELETE_BUTTON).click()

                back_button = self.browser.find_element(*EmployeesPageLocators.BACK_BUTTON).click()

            open("pages/data/test_employees.json","w").close()