from selenium.webdriver.common.by import By

class MainLink():
    LINK = "https://ems.biacorp.ru/"
    DIRECTORIES_LINK = "https://ems.biacorp.ru/directories"

class MainPageLocators():
    LOGIN_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[1]/div[3]/button[1]")

class LoginPageLocators():
    E_MAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_USER = (By.XPATH, "/html/body/div[3]/div[3]/div/section/div/form/div/button")

class ProfilePageLocators():
    LOGO = (By.XPATH, "/html/body/div[1]/div/div[1]/a/div")
    USER_ICON_DROPDOWN = (By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/button")

    OPEN_SEЕTING_PROFILE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]")

    EDITING_PROFILE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/button")
    CURRENT_FIRST_NAME = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div[1]/input")
    CURRENT_PHONE_NUMBER = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div[4]/input")
    SAVE_EDITING_PROFILE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/form/div[7]/button[1]")

    CHANGED_FIRST_NAME = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div[1]/input")
    CHANGED_PHONE_NUMBER = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/div[4]/input")

class EmployeesPageLocators():
    EMPLOYEES_LIST_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[1]/div/button[3]")
    CREATE_EMPLOYEE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/button")
    ADD_MANUALLY = (By.XPATH, "/html/body/div[3]/div[3]/div/section/div/div/a[1]")
    FIRST_NAME = (By.NAME, "surname")
    LAST_NAME = (By.NAME, "name")
    PERSONNEL_NUMBER = (By.NAME, "personnel_number")
    PHONE_NUMBER = (By.NAME, "phone")

    SHIFT = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[3]/div/div[1]/div/div/div/div/div[2]/div")
    SELECT_SHIFT = (By.XPATH, "//div[text()='Смена для теста']")
    SHIFT_START = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[3]/div/div[2]/div/div[2]/div[1]/input")
    OK_SHIFT_START = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[2]/ul/li/button")
    SHIFT_END = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[3]/div/div[2]/div/div[2]/div[3]/input")
    OK_SHIFT_END = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div[2]/ul/li/button")

    FINALLY_CREATE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[5]/button[1]")

    CANCEL_EMPLOYEE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[5]/button[2]")
    CANCEL_ADD_MANUALLY = (By.XPATH, "/html/body/div[3]/div[3]/div/section/button")
    BACK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/a")

    EMPLOYEE_PROFILE = (By.XPATH, "//p[text()='777']")
    EDITING_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]")
    EDITING_SAVE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/button[1]")
    DELETE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/button[2]")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div[5]/div/div/div")

    FIRST_NAME_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[1]/div/div[1]/p")
    LAST_NAME_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[1]/div/div[2]/p")
    PERSONNEL_NUMBER_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div[1]/p")

class DirectoriesPageLocators():
    DROPDOWN_DIRECTORIES_LIST = (By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/div/a[3]/button")

    OBJECT_LIST = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/a[1]")
    ADD_OBJECT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/a")
    CREATE_OBJECT_NAME = (By.NAME, "name")
    CREATE_OBJECT_ADRESS = (By.NAME, "address_line")
    CREATE_CONTACT_PERSON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div/div/div[1]/div[2]")
    SELECT_CONTACT_PERSON = (By.ID, "react-select-2-option-0")
    CREATE_OBJECT_PHONE = (By.NAME, "phone")
    CREATE_OBJECT_EMAIL = (By.NAME, "email")
    CREATE_SHIFT_NAME = (By.NAME, "shifts.0.name")
    CREATE_SHORT_NAME = (By.NAME, "shifts.0.short_name")
    CREATE_START_SHIFT = (By.NAME, "shifts.0.start")
    OK_START_SHIFT = (By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/ul/li[2]/button")
    CREATE_END_SHIFT = (By.NAME, "shifts.0.end")
    OK_END_SHIFT = (By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/ul/li[2]/button")
    CREATE_OBJECT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/button")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div[5]/div/div/div")

    OPEN_OBJECT_PROFILE = (By.XPATH, "//p[text()='Тестовый объект']")
    EDITING_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/button[1]")
    CLEAR_OBJECT_ADRESS = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/input")
    SAVE_EDITING_OBJECT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[3]/button[1]")

    OBJECT_NAME_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div/div[1]/div[1]/p")
    ADDRESS_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div/div[1]/div[2]/p")

    CANCEL_OBJECT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/a")
    CANCEL_ARROW_OBJECT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/a")

    DELETE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/div[2]/button[2]")

    TASK_LIST = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/a[2]")
    ADD_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/a")
    CREATE_TASK_NAME = (By.NAME, "name")
    CREATE_TASK_DESCRIPTION = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/textarea")
    CREATE_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/button")

    NAME_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/p[2]")
    DESCRIPTION_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/p[2]")

    OPEN_TASK_PROFILE = (By.XPATH, "//p[text()='Тестовое описание']")
    SAVE_EDITING_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button[1]")

    CANCEL_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/a")
    CANCEL_ARROW_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/a")

    TASK_EDITING_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/button[1]")
    TASK_DELETE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/button[2]")

    QUALIFICATION_LIST = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/a[3]")
    ADD_QUALIFICATION_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/a")
    CREATE_QUALIFICATION_NAME = (By.NAME, "name")
    CREATE_QUALIFICATION_PAYMENT = (By.NAME, "payment_rate")
    CREATE_QUALIFICATION_PAYMENT_RATE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[2]/div[2]/div/div/div[2]/div")
    SELECT_QUALIFICATION_PAYMENT_RATE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[2]/div[2]/div/div[2]/div/div[2]")
    PLAN_COUNT = (By.NAME, "plan_count")
    CREATE_QUALIFICATION_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[4]/button")

    OPEN_QUALIFICATION_PROFILE = (By.XPATH, "//p[text()='Тестовая специальность']")
    SAVE_EDITING_QUALIFICATION_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/button[1]")

    CANCEL_QUALIFICATION_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div/div[4]/a")
    CANCEL_ARROW_QUALIFICATION_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/a")

    QUALIFICATION_EDITING_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/button[1]")
    QUALIFICATION_DELETE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/button[2]")

    SHIFT_LIST = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/a[4]")
    OPEN_SHIFT_PROFILE = (By.XPATH, "//p[text()='Тестовое описание']")

    ADD_SHIFT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/a")
    ADD_SHIFT_NAME = (By.NAME, "name")
    ADD_SHIFT_DESCRIPTION = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/textarea")
    FINALLY_CREATE_SHIFT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button")

    SHIFT_NAME_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/p[2]")

    CANCEL_SHIFT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[2]/a")
    CANCEL_ARROW_SHIFT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/a")

    SHIFT_EDITING_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/button[1]")
    SAVE_EDITING_SHIFT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/button[1]")
    SHIFT_DELETE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/button[2]")

class BrigadesPageLocators():

    BRIGADES_LIST = (By.XPATH, "/html/body/div[1]/div/div[1]/div/button[4]")
    BRIGADES_PROFILE = (By.XPATH, "//p[text()='+7 911 777 66 61']")

    CREATE_BRIGADE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/a")
    BRIGADE_NAME = (By.NAME, "name")
    BRIGADE_BRIGADIER = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[2]/div/div/div/div[2]/div")
    SELECT_BRIGADE_BRIGADIER = (By.XPATH, "//div[text()='Петров Николай']")
    BRIGADE_OBJECT = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[3]/div/div/div/div[2]/div")
    SELECT_BRIGADE_OBJECT = (By.XPATH, "//div[text()='Тестовый объект']")
    NEXT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[4]/button")
    ADD_EMPLOYEES_MENU = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/button")
    SEARCH_EMPLOYEE = (By.XPATH, "/html/body/div[3]/div[3]/div/section/div/div[1]/div/input")
    ADD_EMPLOYEE = (By.XPATH, "/html/body/div[3]/div[3]/div/section/div/div[3]/div/div/div[2]/button")
    SAVE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[3]/button[1]")

    EDITING_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/button[1]")
    SAVE_EDITING_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/button[1]")

    CANCEL_BRIGADE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[4]/a")
    CANCEL_ARROW_BRIGADE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/a")

    DELETE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/button[2]")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div[5]/div/div/div")

    BRIGADE_EMPLOYEES = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]")
    ADD_BRIGADE_EMPLOYEES = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/button")
    SEARCH_BRIGADE_EMPLOYEE = (By.XPATH, "/html/body/div[3]/div[3]/div/section/div/div[1]/div/input")
    ADD_BRIGADE_EMPLOYEES_BUTTON = (By.XPATH, "/html/body/div[3]/div[3]/div/section/div/div[3]/div/div/div[2]/button")

    DELETE_EMPLOYEE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/button")

class TaskPageLocators():

    TASKS_LIST = (By.XPATH, "/html/body/div[1]/div/div[1]/div/button[2]")
    TASK_PROFILE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/a")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div[5]/div/div/div")

    ADD_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/a")
    TYPE_TASK = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[1]/div/div/div/div[2]/div")
    SELECT_TYPE_TASK = (By.XPATH, "//div[text()='Доп. смена']")
    TASK_ADDITIONAL_DESCRIPTION = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[2]/textarea")
    NUMBER_OF_EMPLOYEES = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[3]/div/input")
    TASK_QUALIFICATION = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[4]/div/div/div/div[2]/div")
    SELECT_TASK_QUALIFICATION = (By.XPATH, "//div[text()='Тестовая специальность']")
    NEXT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[5]/button")

    TASK_DATE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[1]/div[1]/div[1]/div/div/input")
    TASK_OBJECT = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div")
    SELECT_TASK_OBJECT = (By.XPATH, "//div[text()='Тестовый объект']")
    SAVE_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[3]/div/button[2]")

    EDITING_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/button[3]")
    NEW_NUMBER_OF_EMPLOYEES = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div/div[1]/div[2]/input")
    SAVE_EDITING_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div/div[2]/button[1]")

    DELETE_TASK_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/button[4]")

    CANCEL_CREATE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/div[5]/a")
    CANCEL_ARROW_CREATE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/a")

    TASK_EMPLOYEE_LIST = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[3]")
    ADD_TASK_EMPLOYEE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[5]/div/button")
    SEARCH_TASK_EMPLOYEE = (By.XPATH, "/html/body/div[3]/div[3]/div/section/div/div[1]/div/input")
    ADD_TASK_EMPLOYEE_BUTTON = (By.XPATH, "/html/body/div[3]/div[3]/div/section/div/div[3]/div/div/div[2]/button")
    REPLACE_TASK_EMPLOYEE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[5]/div/div[2]/div[5]/button")

    EMPLOYEES_NUMBER_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/form/div/div/p[2]")

class ShiftSchedulePageLocators():
    
    SCHEDULE_PAGE = (By.XPATH, "/html/body/div[1]/div/div[1]/div/button[1]")

    EMPLOYEE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/a")

    DEFICIT_MENU_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[2]")
    DEFICIT_MENU = (By.XPATH, "/html/body/div[3]/div[3]/div/section")
    X_BUTTON = (By.XPATH, "/html/body/div[3]/div[3]/div/section/button")
    CANCEL_BUTTON = (By.XPATH, "/html/body/div[3]/div[3]/div/section/form/div[2]/button[2]")