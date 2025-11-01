from selenium.webdriver.common.by import By

class Logos_locators: 
    LOGO_SCOOTER = [By.XPATH, "//img[@alt = 'Scooter']"]
    LOGO_YANDEX = [By.XPATH, "//img[@alt = 'Yandex']"]
    LOGO_DZEN = [By.XPATH, "//*[contains(@class, 'header__logoLink')]"]