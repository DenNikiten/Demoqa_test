import base64
import os
import random
import time
import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesPageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("Fill in all fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step('filing fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('go to submit button'):
            self.go_to_element(self.element_is_visible(self.locators.MOVE_TO_SUBMIT_BUTTON))
        with allure.step('click submit button'):
            self.element_is_clickable(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('check filled form')
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('click random items')
    def click_random_checkbox(self, count):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        for _ in range(count):
            item = item_list[random.randint(1, 15)]
            self.go_to_element(item)
            item.click()

    @allure.step('get checked checkbox')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(".", "").replace(" ", "").replace("doc", "").lower()

    @allure.step('get output result')
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(" ", "").lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('click on the radiobutton')
    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    @allure.step('get output result')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    @allure.step('add new person')
    def add_new_person(self, count):
        data = []
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.first_name
            lastname = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_clickable(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.go_to_element(self.element_is_visible(self.locators.SUBMIT))
            self.element_is_clickable(self.locators.SUBMIT).click()
            count -= 1
            data.append([firstname, lastname, str(age), email, str(salary), department])
        return data

    @allure.step('get added person')
    def get_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('check added person')
    def check_new_added_person(self):
        new_person = self.add_new_person(3)
        table_result = self.get_new_added_person()
        assert all([el in table_result for el in new_person]) == True

    @allure.step('find some person')
    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('get search person')
    def get_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('go to search input')
    def go_to_search_input(self):
        self.go_to_element(self.element_is_clickable(self.locators.GO_TO_SEARCH_INPUT))

    @allure.step('check found person')
    def check_search_person(self):
        key_word = self.add_new_person(2)[0][random.randint(0, 5)]
        self.go_to_search_input()
        self.search_some_person(key_word)
        table_result = self.get_search_person()
        assert key_word in table_result, 'The person was not found in the table'

    @allure.step('update person information')
    def update_person_info(self):
        person_info = next(generated_person())
        choices = {"firstname": (person_info.first_name, self.locators.FIRSTNAME_INPUT),
                   "lastname": (person_info.last_name, self.locators.LASTNAME_INPUT),
                   "email": (person_info.email, self.locators.EMAIL_INPUT),
                   "age": (person_info.age, self.locators.AGE_INPUT),
                   "salary": (person_info.salary, self.locators.SALARY_INPUT),
                   "department": (person_info.department, self.locators.DEPARTMENT_INPUT)}
        choice_key_word = random.choice(("firstname", "lastname", "email", "age", "salary", "department"))
        random_person_info = choices[choice_key_word][0]
        random_person_info_locator = choices[choice_key_word][1]
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(random_person_info_locator).clear()
        self.element_is_visible(random_person_info_locator).send_keys(random_person_info)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(random_person_info)

    @allure.step('delete person')
    def delete_person(self):
        self.element_is_present(self.locators.DELETE_BUTTON).click()

    @allure.step('check deleted person')
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('clear field search input')
    def clear_field_search_input(self):
        self.clear_field(self.locators.SEARCH_INPUT)

    @allure.step('check count rows')
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

    @allure.step('select up to some rows')
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for el in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{el}"')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('select up to some rows method select')
    def select_up_to_some_rows_method_select(self):
        select = Select(self.element_is_visible(self.locators.COUNT_ROW_LIST))
        count = ['5', '10', '20', '25', '50', '100']
        data = []
        for el in count:
            select.select_by_value(el)
            data.append(self.check_count_rows())
        return data


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step('check clicked button')
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text

    @allure.step('click on different  buttons')
    def click_on_different_button(self, type_click):
        buttons = {"double": (self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON)),
                              self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)),
                   "right": (self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)),
                             self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)),
                   "click": (self.element_is_clickable(self.locators.CLICK_ME_BUTTON).click(),
                             self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME))}
        click = buttons[type_click][0]
        success_text = buttons[type_click][1]
        return success_text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step('check simple link')
    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.switch_to_new_tab(1)
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    @allure.step('check broken link')
    def check_broken_link(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return r.status_code


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    @allure.step('upload file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    @allure.step('download file')
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = os.getcwd() + rf'\file_test_{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
        os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step('check enable button')
    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step('check changed of color')
    def check_changed_of_colour(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    @allure.step('check appear of button')
    def check_appear_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True
