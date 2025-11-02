import allure
import pytest
from pages.page_order import OrderPage
from pages.page_main import MainPage
from data import BrowserUrl, client_info

class TestPageOrder: 
    @allure.title('Тестирование создания заказа с помощью кнопки "Заказать" в шапке профиля')
    @pytest.mark.parametrize(
        "name, last_name, address, metro, rent_period, colour, comment",
        [
            (client_info['name'][0],
             client_info['last_name'][0],
             client_info['adress'][0],
             client_info['metro'][0],
             client_info['rent_period'][0],
             client_info['colour'][0], 
             client_info['comment'][0])
        ]
    )
    
    def test_create_order_button_down(self, driver, name, last_name, address, metro, rent_period, colour, comment):
        driver.get(BrowserUrl.main_url)
        page_order = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.create_order_button_down()
        page_order.fill_form_about_info_client(name, last_name, address, metro)
        page_order.fill_form_about_rent(rent_period, colour, comment)
        page_order.confirmation_order()
        assert 'Посмотреть статус' in page_order.check_accept_order()


    @allure.title('Тестирование создания заказа с помощью кнопки "Заказать" внизу страницы')
    @pytest.mark.parametrize(
        "name, last_name, address, metro, rent_period, colour, comment",
        [
            (client_info['name'][1],
             client_info['last_name'][1],
             client_info['adress'][1],
             client_info['metro'][1],
             client_info['rent_period'][1],
             client_info['colour'][1],
             client_info['comment'][1])
        ]
    )

    def test_create_order_button_up(self, driver, name, last_name, address, metro, rent_period, colour, comment):
        driver.get(BrowserUrl.main_url)
        page_order = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.created_order_button_up()
        page_order.fill_form_about_info_client(name, last_name, address, metro)
        page_order.fill_form_about_rent(rent_period, colour, comment)
        page_order.confirmation_order()
        assert 'Посмотреть статус' in page_order.check_accept_order()
