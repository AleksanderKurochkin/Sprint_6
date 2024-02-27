from pages.base_page import BasePage
from locators.page_order_scooter_locators import PageOrderScooterLocators
from data import Data, Url
import allure

class PageOrderScooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполняем форму "Для кого самокат"')
    def complete_form_one(self):
        self.enter_text(PageOrderScooterLocators.FIELD_NAME, Data.NAME)
        self.enter_text(PageOrderScooterLocators.FIELD_FIRSTNAME, Data.FIRSTNAME)
        self.enter_text(PageOrderScooterLocators.FIELD_ADDRESS, Data.ADDRESS)
        self.click_on_element(PageOrderScooterLocators.FIELD_METRO)
        self.click_on_element(PageOrderScooterLocators.METRO)
        self.enter_text(PageOrderScooterLocators.FIELD_TELEPHONE, Data.TELEPHONE)

    @allure.step('Заполняем форму "Про аренду"')
    def complete_form_two(self):
        self.click_on_element(PageOrderScooterLocators.FIELD_DATE)
        self.click_on_element(PageOrderScooterLocators.DATA)
        self.click_on_element(PageOrderScooterLocators.FIELD_RETAIL_PERIOD)
        self.click_on_element(PageOrderScooterLocators.TWO_DAYS)
        self.click_on_element(PageOrderScooterLocators.COLOUR_SCOOTER)
        self.enter_text(PageOrderScooterLocators.COMMENT, Data.COMMENT)

    @allure.step('Открываем страницу заказа самоката')
    def open_order_page(self):
        self.open_page(Url.URL_PAGE_ORDER)





