import allure
from locators.page_main_menu_locators import MainMenu
from pages.base_page import BasePage


class MainPage(BasePage): 
   
    @allure.step('Принимаем куки')
    def accept_cookie(self):
        self.click_to_element(MainMenu.BUTTON_COOKIE)

    @allure.step('Создаем заказ с помощью кнопки "Заказать" в шапке профиля')
    def created_order_button_up(self):
        return self.click_to_element(MainMenu.BUTTON_ORDER_UP)
    
    @allure.step('Пролистываем страницу до кнопки "Заказать" внизу страницы')
    def scroll_for_order_button_down(self): 
        button_order_down = self.find_element_with_wait(MainMenu.BUTTON_ORDER_DOWN)
        self.scroll_for_element(button_order_down)

    @allure.step('Нажимаем на кнопку "Заказать" внизу страницы')
    def click_for_order_button_down(self):
        self.click_to_element(MainMenu.BUTTON_ORDER_DOWN)

    @allure.step('Создаем заказ с помощью кнопки "Заказать" внизу страницы')
    def create_order_button_down(self):
        self.scroll_for_order_button_down()
        self.click_for_order_button_down()

    @allure.step('Пролистываем страницу до последнего вопроса')
    def scroll_for_last_question(self): 
        last_question = self.find_element_with_wait(MainMenu.LAST_QUESTION)
        self.scroll_for_element(last_question)

    @allure.step('Нажимаем на вопрос')
    def click_to_question(self, question_id): 
        locator_question = self.format_locators(MainMenu.QUESTION_NUMBER, question_id)
        self.click_to_element(locator_question)

    @allure.step('Получаем текст с вопроса')
    def get_question_text(self, question_id):
        locator_question = self.format_locators(MainMenu.QUESTION_NUMBER, question_id)
        return self.get_text_from_element(locator_question)
    
    @allure.step('Проверяем текст вопроса в соответствии с его id')
    def check_question(self, question_id):
        self.scroll_for_last_question()
        return self.get_question_text(question_id)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, question_id):
        locator_answer = self.format_locators(MainMenu.ANSWER_NUMBER, question_id)
        return self.get_text_from_element(locator_answer)

    @allure.step('Проверяем текст ответа в соответствии id вопроса')
    def check_answer_for_question(self, question_id):
        self.click_to_question(question_id)
        return self.get_answer_text(question_id)