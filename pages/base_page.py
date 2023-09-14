from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    """Метод для поиска видимого элемента"""
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    """Метод для поиска видимовых элементов"""
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    """Метод для поиска элемента(текст к примеру) из дом-дерева"""
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    """Проверка на кликабельность"""
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    """Метод для скроллинга до нужного элемента"""
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()


    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    """Метод для удаления футера"""

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();") #удаляем баннер
        self.driver.execute_script("document.getElementById('close-fixedban').remove();") #удаляем кнопку под баннером

    """Метод для управления в новой вкладке"""

    def switch_new_tab(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)