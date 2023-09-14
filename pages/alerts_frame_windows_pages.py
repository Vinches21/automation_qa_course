from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self, choise: int):
        buttons = {1: self.element_is_visible(self.locators.NEW_TAB_BUTTON),
                   2: self.element_is_visible(self.locators.NEW_WINDOW_BUTTON)}
        buttons[choise].click()
        self.switch_new_tab()
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title



