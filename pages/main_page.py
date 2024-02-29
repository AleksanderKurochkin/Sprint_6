from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Url
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open_page(Url.URL_PAGE_MAIN)

    @allure.step("Берем URL главной страницы")
    def expected_url_main(self, url=Url.URL_PAGE_MAIN):
        return url

    @allure.step("Берем URL страницы DZEN")
    def expected_url_dzen(self, url_dzen=Url.URL_PAGE_DZEN):
        return url_dzen

    @allure.step('Нажимаем на вопрос')
    def click_to_question_and_get_answer(self, locator_q, locator_a, num):
        method_q, locator_qq = locator_q
        method_a, locator = locator_a
        locator_qq = locator_qq.format(num)
        locator = locator.format(num)
        self.click_on_element((method_q, locator_qq))
        return self.get_text_from_element((method_a, locator))

    @allure.step('Получаем ответ')
    def get_answer(self, q_nam):
        result = self.click_to_question_and_get_answer(
            MainPageLocators.QUESTION,
            MainPageLocators.ANSWER, q_nam)
        return result

    @allure.step('Проверяем ответ')
    def check_answer(self, result, expected):
        return result == expected
