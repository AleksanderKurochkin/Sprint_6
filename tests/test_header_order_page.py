from data import Url
from pages.header_page_order import HeaderPagesOrder
from pages.page_order_scooter import PageOrderScooter
import allure
class TestHeaderOrderScooter:

    @allure.title('Проверка перехода по кнопкам хедера')
    @allure.description('Переход на главную страницу при нажатии на логотип scooter в хедере')
    def test_open_main_page_button_scooter(self, browser_firefox):
        header_page_order = HeaderPagesOrder(browser_firefox)
        page_order_scooter = PageOrderScooter(browser_firefox)

        page_order_scooter.open_order_page()
        actual_url = header_page_order.click_on_button_scooter_and_get_url()
        expected_url = Url.URL_PAGE_MAIN
        assert actual_url == expected_url

    @allure.description('Переход на страницу dzen в новой вкладке при нажатии логотип yandex в хедере')
    def test_open_dzen_page_button_yandex(self, browser_firefox):
        header_page_order = HeaderPagesOrder(browser_firefox)
        page_order_scooter = PageOrderScooter(browser_firefox)

        page_order_scooter.open_order_page()
        actual_url = header_page_order.click_on_button_yandex_open_new_tab_dzen()
        expected_url = Url.URL_PAGE_DZEN
        assert actual_url == expected_url
