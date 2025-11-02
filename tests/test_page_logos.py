import allure
from pages.page_logos import LogoPage
from pages.page_main import MainPage
from data import BrowserUrl


class TestLogos: 
    @allure.title('Проверка перехода на главную страницу сайта "Самокат" при нажатии на логотип Самоката')
    def test_transition_an_main_page_by_click_on_scooter_logo(self, driver):
        driver.get(BrowserUrl.main_url)
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.created_order_button_up()
        logo_page = LogoPage(driver)
        logo_page.switch_to_scooter_page()
        assert driver.current_url == BrowserUrl.main_url

    @allure.title('Проверка перехода на страницу "Яндекс Дзен" при нажати на логотип Яндекса')
    def test_transition_an_yandex_page_by_click_on_yandex_logo(self, driver):
        driver.get(BrowserUrl.main_url)
        main_page = MainPage(driver)
        main_page.accept_cookie()
        yandex_page = LogoPage(driver)
        yandex_page.switch_to_yandex_page()
        assert driver.current_url == BrowserUrl.yandex_url
