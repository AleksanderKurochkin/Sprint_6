import time

from locators.header_page_order_locators import HeaderPageOrderLocators
from pages.base_page import BasePage

class HeaderPagesOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_button_scooter_and_get_url(self):
        self.click_on_element(HeaderPageOrderLocators.HEADER_SCOOTER)
        return self.driver.current_url

    def click_on_button_yandex_open_new_tab_dzen(self):
        self.click_on_element(HeaderPageOrderLocators.HEADER_YANDEX)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        time.sleep(5)
        return self.driver.current_url

