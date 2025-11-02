import allure
from locators.page_order_locators import OrderPageLocators
from helpers import generate_delivery_date, generate_random_phone
from pages.base_page import BasePage



class OrderPage(BasePage): 

    @allure.step('заполняем поле "Имя"')
    def set_name(self, name): 
        self.add_text_to_element(OrderPageLocators.USER_NAME, name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_last_name(self, last_name): 
        self.add_text_to_element(OrderPageLocators.LAST_NAME, last_name)

    @allure.step('Заполняем поле адрес')
    def set_address(self, address): 
        self.add_text_to_element(OrderPageLocators.ADDRESS_USER, address)

    @allure.step('Заполняем поле Метро')
    def set_metro_station(self, metro): 
        self.add_text_to_element(OrderPageLocators.METRO_STATION, metro)
        self.click_to_element(OrderPageLocators.SELECT_METRO_STATION)

    @allure.step('Заполняем поле "Телефон"')
    def set_number(self): 
        number_user = generate_random_phone()
        self.add_text_to_element(OrderPageLocators.NUMBER_USER, number_user)

    @allure.step('Нажимаем кнопку "Далее"')
    def click_to_buttom_next(self): 
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполняем форму "Для кого самокат и переходим на следующую страницу')
    def fill_form_about_info_client(self, name, last_name, address, metro):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro_station(metro)
        self.set_number()
        self.click_to_buttom_next()

    @allure.step('заполняем поле "Когда привезти заказ"')
    def set_date_rent(self): 
        date_delivery = generate_delivery_date()
        self.add_text_to_element(OrderPageLocators.DATE_DELIVERY, date_delivery)

    @allure.step('Заполняем поле "Срок аренды"')
    def set_rental_period(self, rent_period):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        locator_rent_period = self.format_locators(OrderPageLocators.DATE_RENTAL_PERIOD, rent_period)
        self.click_to_element(locator_rent_period)

    @allure.step('Выбираем чек-бокс по цвету самоката')
    def choose_color_for_scooter(self, colour):
        locator_colour = self.format_locators(OrderPageLocators.CHECKBOX_COLOR, colour)
        self.click_to_element(locator_colour)

    @allure.step('Заполняем поле "Комментарий"')
    def set_comment(self, comment): 
        self.add_text_to_element(OrderPageLocators.COMMENT_ORDER, comment)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_to_button_order(self):
        self.click_to_element(OrderPageLocators.BUTTON_ORDER) 

    @allure.step('Заполняем форму "про аренду" и создаем заказ')
    def fill_form_about_rent(self, rent_period, colour, comment): 
        self.set_date_rent()
        self.set_rental_period(rent_period)
        self.choose_color_for_scooter(colour)
        self.set_comment(comment)
        self.click_to_button_order()

    @allure.step('Подтверждаем заказ')
    def confirmation_order(self): 
        self.click_to_element(OrderPageLocators.BUTTON_CONFIRMATION_YES)

    @allure.step('Получаем подтверждение заказа')
    def check_accept_order(self): 
        return self.get_text_from_element(OrderPageLocators.TITLE_ORDER_ADD)