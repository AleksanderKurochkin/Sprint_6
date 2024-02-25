import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.page_order_scooter import PageOrderScooterLocators
from pages.page_order_scooter import PageOrderScooter

class TestOrderScooter:
    @allure.title('Проверка формы заказа самоката')
    @allure.description('Проверяем заказ самоката через две кнопки заказать, на главном экране')
    @pytest.mark.parametrize('button_order', [
                             MainPageLocators.BUTTON_ORDER_HIGH,
                             MainPageLocators.BUTTON_ORDER_LOWER])
    def test_order_scooter_button_high(self, browser_firefox, button_order):
        main_page = MainPage(browser_firefox)
        base_page = BasePage(browser_firefox)
        page_order_scooter = PageOrderScooter(browser_firefox)

        main_page.open_main_page()
        base_page.click_on_element(button_order)

        page_order_scooter.complete_form_one()
        base_page.click_on_element(PageOrderScooterLocators.BUTTON_FORTH)

        page_order_scooter.complete_form_two()
        base_page.click_on_element(PageOrderScooterLocators.BUTTON_ORDER)

        base_page.click_on_element(PageOrderScooterLocators.BUTTON_YES)

        assert base_page.get_text_from_element(PageOrderScooterLocators.BUTTON_STATUS) == "Посмотреть статус"







