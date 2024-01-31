import time
from random import randint as rd

from pages.alerts_frame_windows_pages import BrowserWindowsPage, AlertsPage, FramePage


class TestAlertsFrameWindow:

    class TestBrowserWindow:

        def test_new_tab_and_new_window(self, driver):
            new_buttons = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_buttons.open()
            text_result = new_buttons.check_opened_new_tab(rd(1, 2))
            assert text_result == "This is a sample page", "The new tab has not opened or incorrect tab has opened"


    class TestAlertsPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'Alert did not show up'

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', 'Alert did not show up'

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, 'Alert did not show up'

    class TestFramePage:

        def test_frames(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame_2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame_2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'
            print(result_frame1)

