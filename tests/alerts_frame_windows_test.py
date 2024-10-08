import allure
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindows:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:

        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_title = browser_windows_page.check_opened_new_tab()
            assert text_title == "This is a sample page", "new tab did not open or wrong tab opened"

        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_title = browser_windows_page.check_opened_new_window()
            assert text_title == "This is a sample page", "new window did not open or wrong window opened"

        @allure.title('Checking the opening of a new window or a new tab')
        def test_new_tab_or_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_title = browser_windows_page.check_opened_new_tab_or_new_window("window")
            assert text_title == "This is a sample page", "new tab or window did not open or wrong tab or window opened"

    @allure.feature('Alerts Page')
    class TestAlerts:
        @allure.title('Checking the opening of an alert')
        def test_see_alerts(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == "You clicked a button", "Alert did not show up"

        @allure.title('Checking the opening of the alert after 5 seconds')
        def test_alert_appear_5_sec(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "Alert did not show up"

        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            text_result = alerts_page.check_confirm_alert()
            assert text_result == "You selected Ok" or text_result == "You selected Cancel", "Alert did not show up"

        @allure.title('Checking the opening of the alert with prompt')
        def test_prompt_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            text, text_result = alerts_page.check_prompt_alert()
            assert text in text_result, "Alert did not show up"

    @allure.feature('Frame Page')
    class TestFrames:
        @allure.title('Check the page with frames')
        def test_frames(self, driver):
            frame_page = FramesPage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame does not exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame does not exist"

    @allure.feature('Nested Page')
    class TestNestedFrames:
        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text, "The nested frame does not exist"
            assert child_text, "The nested frame does not exist"

    @allure.feature('Modal Dialog Page')
    class TestModalDialogs:
        @allure.title('Check the page with a small modal dialogs')
        def test_small_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            text_small_modal, title_small_modal = modal_dialogs_page.check_small_modal_dialogs()
            assert text_small_modal == 47, "text doesn't match"
            assert title_small_modal == "Small Modal", "The title is not 'Small Modal'"

        @allure.title('Check the page with a large modal dialogs')
        def test_large_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            text_large_modal, title_large_modal = modal_dialogs_page.check_large_modal_dialogs()
            assert text_large_modal == 574, "text doesn't match"
            assert title_large_modal == "Large Modal", "The title is not 'Large Modal'"
