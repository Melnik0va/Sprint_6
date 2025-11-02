from selenium.webdriver.common.by import By

class OrderPageLocators(): 
    TITLE_PAGE_ORDER = [By.XPATH, "//div[text()='Для кого самокат']"]
    USER_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_USER = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_STATION = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    SELECT_METRO_STATION = [By.XPATH, "//div[@class='select-search__select']"]
    NUMBER_USER = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_NEXT = [By.XPATH, "//button[text()='Далее']"]

    TITLE_PAGE_RENTAL = [By.XPATH, "//div[text()='Про аренду']"]
    DATE_DELIVERY = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENTAL_PERIOD = [By.XPATH, "//span[@class='Dropdown-arrow']"]
    DATE_RENTAL_PERIOD = [By.XPATH, "//div[@class='Dropdown-option' and text()='{}']"]
    CHECKBOX_COLOR = [By.XPATH, "//input[@id='{}']"]
    COMMENT_ORDER = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    BUTTON_ORDER = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"]

    TITLE_CONFIRMATION_WINDOW = [By.XPATH, "//div[text()='Хотите оформить заказ?']"]
    BUTTON_CONFIRMATION_YES = [By.XPATH, "//button[text()='Да']"]
    TITLE_ORDER_ADD = [By.XPATH, "//button[text()='Посмотреть статус']"]
    
    