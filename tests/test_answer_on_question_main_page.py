from data import Answers
from pages.main_page import MainPage
import pytest
import allure

class TestMainPage:
    @allure.title('Проверка корректного текста на форме вопрос-ответ')
    @pytest.mark.parametrize(
        "q_nam, expected_result",
        [
            (0, Answers.ANSWER_0),
            (1, Answers.ANSWER_1),
            (2, Answers.ANSWER_2),
            (3, Answers.ANSWER_3),
            (4, Answers.ANSWER_4),
            (5, Answers.ANSWER_5),
            (6, Answers.ANSWER_6),
            (7, Answers.ANSWER_7)
        ]
    )
    def test_answer_on_question_main_page(self, browser_firefox, q_nam, expected_result):
        main_page = MainPage(browser_firefox)
        main_page.open_main_page()
        assert main_page.check_answer(main_page.get_answer(q_nam), expected_result)
