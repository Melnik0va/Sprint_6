from selenium.webdriver.common.by import By

class MainMenu: 
    LOGO_MAIN_MENU = [By.XPATH, "//img[@alt='Scooter']"]
    LOGO_YANDEX = [By.XPATH, "//img[@alt='Yandex']"]
    BUTTON_ORDER_UP = [By.XPATH,  "//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g' and text()='Заказать']"]
    BUTTON_ORDER_DOWN = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"]
    BUTTON_SCROLL_DOWN = [By.XPATH, "//img[@alt=Scroll down]"]
    TITLE_COOKIE = [By.XPATH, "//div[contains(@class,'App_CookieText') and text()='И здесь куки! В общем, мы их используемю']"]
    BUTTON_COOKIE = [By.XPATH, "//button[text()='да все привыкли']"]

    QUESTION_NUMBER = [By.XPATH, "//div[@id='accordion__heading-{}']"]
    ANSWER_NUMBER = [By.XPATH, "//div[@id='accordion__panel-{}']/p"]
    LAST_QUESTION = [By.XPATH, "//div[@id='accordion__heading-7']"]