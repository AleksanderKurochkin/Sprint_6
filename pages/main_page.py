from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def click_to_question_and_get_answer(self, locator_q, locator_a, num):
        method_q, locator_qq = locator_q
        method_a, locator = locator_a
        locator_qq = locator_qq.format(num)
        locator = locator.format(num)
        self.click_on_element((method_q, locator_qq))
        return self.get_text_from_element((method_a, locator))

    def check_answer(self, result, expected):
        return result == expected


