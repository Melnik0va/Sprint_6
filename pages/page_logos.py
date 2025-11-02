import allure
from locators.page_logos_locators import Logos_locators
from pages.base_page import BasePage


class LogoPage(BasePage): 

    @allure.step('Проверка отображения логотипа Самоката на главной странице Самоката')
    def check_logo_scooter(self):
        self.find_element_with_wait(Logos_locators.LOGO_SCOOTER)

    @allure.step('Нажатие на логотип Самоката')
    def click_logo_scooter(self):
        self.click_to_element(Logos_locators.LOGO_SCOOTER)

    @allure.step('Переход на главную страницу Самоката')
    def switch_to_scooter_page(self):
        self.check_logo_scooter()
        self.click_logo_scooter()

    @allure.step('Проверка отображения логотоипа Яндекса на главной страницу Самоката')
    def check_logo_yandex(self): 
        self.find_element_with_wait(Logos_locators.LOGO_YANDEX)

    @allure.step('Нажатие на логотип Яндекса')
    def click_logo_yandex(self):
        self.click_to_element(Logos_locators.LOGO_YANDEX)

    @allure.step('Переход на последнюю открывшеюся вкладку браузера')
    def switch_last_page(self):
        self.switch_window()

    @allure.step('Проверка отображения логотипа Яндекс Дзена')
    def check_logo_dzen(self):
        self.find_element_with_wait(Logos_locators.LOGO_DZEN)

    @allure.step('Переход на главную страницу Яндекса')
    def switch_to_yandex_page(self):
        self.check_logo_yandex()
        self.click_logo_yandex()
        self.switch_last_page()
        self.check_logo_dzen()
        