import random
import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent address does not match"
            time.sleep(2)

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox(21)
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "checkboxes have not been selected"

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"

    class TestWebTables:

        def test_web_tables_add_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            web_tables_page.check_new_added_person()

        def test_web_table_search_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            web_tables_page.check_search_person()

        def test_web_tables_update_person_info(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            key_word = web_tables_page.add_new_person(2)[0][random.randint(0, 5)]
            web_tables_page.go_to_search_input()
            web_tables_page.search_some_person(key_word)
            random_person_info = web_tables_page.update_person_info()
            row = web_tables_page.get_search_person()
            assert random_person_info in row, "the person card was not changed"

        def test_web_tables_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            key_word = web_tables_page.add_new_person(2)[0][random.randint(0, 5)]
            web_tables_page.go_to_search_input()
            web_tables_page.clear_field_search_input()
            web_tables_page.search_some_person(key_word)
            web_tables_page.delete_person()
            web_tables_page.go_to_search_input()
            web_tables_page.clear_field_search_input()
            web_tables_page.search_some_person(key_word)
            text = web_tables_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            count = web_tables_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "The number of rows in the table " \
                                                      "has not been changed or has changed incorrectly"

        def test_web_table_change_count_row_select_method(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            count = web_tables_page.select_up_to_some_rows_method_select()
            assert count == [5, 10, 20, 25, 50, 100], "The number of rows in the table " \
                                                      "has not been changed or has changed incorrectly"

    class TestButtons:

        def test_different_click_on_the_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_on_different_button('double')
            right = buttons_page.click_on_different_button('right')
            click = buttons_page.click_on_different_button('click')
            assert double == 'You have done a double click', "The double click button was not pressed"
            assert right == 'You have done a right click', "The right click button was not pressed"
            assert click == 'You have done a dynamic click', "The dynamic click button was not pressed"

    class TestLinks:

        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link("https://demoqa.com/bad-request")
            assert response_code == 400, "the links works or the status code not 400"

    class TestUploadAndDownload:

        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "the file has not been upload"

        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "the file has not been downloaded"

    class TestDynamicProperties:

        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, "button did not enable after 5 second"

        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_colour()
            assert color_before != color_after, "colors have not benn changed"

        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True, "button did not appear after 5 second"
