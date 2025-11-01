import allure
import pytest
from pages.page_main import MainPage
from data import BrowserUrl
from data import test_data

class TestPageQuestions:
    
    @allure.title('Проверка выпадающего списка вопросов и ответов')
    @pytest.mark.parametrize(
        "question_id, expected_question, expected_answer",
        test_data
    )
    def test_questions_and_answers(self, driver, question_id, expected_question, expected_answer):
        driver.get(BrowserUrl.main_url)
        main_page = MainPage(driver)
        main_page.accept_cookie()

        # Проверяем вопрос
        actual_question = main_page.check_question(question_id)
        assert actual_question == expected_question, (
            f"Вопрос для ID {question_id} не совпадает. "
            f"Ожидаемо: '{expected_question}', получено: '{actual_question}'"
        )

        # Проверяем ответ
        actual_answer = main_page.check_answer_for_question(question_id)
        assert actual_answer == expected_answer, (
            f"Ответ для ID {question_id} не совпадает. "
            f"Ожидаемо: '{expected_answer}', получено: '{actual_answer}'"
        )