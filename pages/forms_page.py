import os
import random
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file, generated_subject
from locators.forms_page_locators import PracticeFormPageLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()

    def fill_practice_form(self):
        person = next(generated_person())
        file_name, path = generated_file()
        # self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(person.mobile_number)
        new_date = self.element_is_visible(self.locators.DATE_OF_BIRTH)
        for _ in range(11):
            new_date.send_keys(Keys.SHIFT + Keys.ARROW_LEFT)
        new_date.send_keys(f'{random.randint(1930, 2006)}-{random.randint(1, 12)}-{random.randint(1, 28)}')
        new_date.send_keys(Keys.RETURN)
        subject = self.element_is_visible(self.locators.SUBJECT)
        subject.send_keys(generated_subject())
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        data = []
        for el in result_list:
            self.go_to_element(el)
            data.append(el.text)
        return data

