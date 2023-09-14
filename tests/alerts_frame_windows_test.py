import time
from random import randint as rd

from pages.alerts_frame_windows_pages import BrowserWindowsPage


class TestAlertsFrameWindow:

    class TestBrowserWindow:

        def test_new_tab_and_new_window(self, driver):
            new_buttons = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_buttons.open()
            text_result = new_buttons.check_opened_new_tab(rd(1, 2))
            assert text_result == "This is a sample page", "The new tab has not opened or incorrect tab has opened"



