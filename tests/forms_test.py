import time

from pages.forms_page import PracticeFormPage


class TestForms:
    class TestPracticeForm:

        def test_practice_form(self, driver):
            practice_form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
            practice_form_page.open()
            p = practice_form_page.fill_practice_form()
            result = practice_form_page.form_result()
            assert [p.first_name + " " + p.last_name, p.email] == [result[0], result[1]], "the form is not filled out"
