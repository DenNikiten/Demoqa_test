import random
import time

from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.switch_to_new_tab(1)
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.switch_to_new_tab(1)
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_tab_or_new_window(self, new_tab_win):
        choice_new_tab_or_window = {'tab': self.element_is_visible(self.locators.NEW_TAB_BUTTON),
                                    'window': self.element_is_visible(self.locators.NEW_WINDOW_BUTTON)}
        choice = choice_new_tab_or_window[new_tab_win]
        choice.click()
        self.switch_to_new_tab(1)
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        alert_window = self.switch_to_alert(self.locators.SEE_ALERT_BUTTON)
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_FIVE_SEC_BUTTON).click()
        time.sleep(5)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        # choices = [alert_window.accept, alert_window.dismiss]
        # random.choice(choices)()
        choices = {1: alert_window.accept, 2: alert_window.dismiss}
        choices[random.randint(1, 2)]()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result
        # try:
        #     text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        #     return text_result
        # except UnexpectedAlertPresentException:
        #     text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        #     return text_result

    def check_prompt_alert(self):
        text = f"autotest{random.randint(10, 800)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_small_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        small_modal_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
        title_small_modal = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        return len(small_modal_text), title_small_modal

    def check_large_modal_dialogs(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        large_modal_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
        title_large_modal = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return len(large_modal_text), title_large_modal


