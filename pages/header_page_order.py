from data import Url
from locators.header_page_order_locators import HeaderPageOrderLocators
from pages.base_page import BasePage
import allure


class HeaderPagesOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем на кнопку "Самокат" в хедере переходим по ссылке и получаем URL страницы')
    def click_on_button_scooter_and_get_url(self):
        self.click_on_element(HeaderPageOrderLocators.HEADER_SCOOTER)
        return self.get_current_url()

    @allure.step('Нажимаем на кнопку "Yandex" в хедере переходим по ссылке, переходим на '
                 'новую вкладку и получаем URL страницы')
    def click_on_button_yandex_open_new_tab_dzen(self):
        self.click_on_element(HeaderPageOrderLocators.HEADER_YANDEX)
        self.open_new_tab()
        self.url_with_wait(Url.URL_PAGE_DZEN)
        return self.get_current_url()
