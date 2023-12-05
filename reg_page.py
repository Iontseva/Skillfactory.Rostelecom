from locators import *
from base_page import BasePage



class RegPage(BasePage):
    def __init__(self, driver,timeout=5):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/"
        driver.get(url)
        driver.find_element(*AuthLocators.AUTH_REGISTER).click()

        #Создаём нужные элементы
        self.name = driver.find_element(*RegLocators.REG_NAME)
        self.lastname = driver.find_element(*RegLocators.REG_LASTNAME)
        self.address = driver.find_element(*RegLocators.REG_ADDRESS)
        self.password = driver.find_element(*RegLocators.REG_PASS)
        self.password_confirm = driver.find_element(*RegLocators.REG_PASS)
        self.btn = driver.find_element(*RegLocators.REG_BTN)

    # Описываем функции для элементов страницы

    def enter_name(self,value):
        self.name.send_keys(value)

    def enter_lastname(self, value):
        self.lastname.send_keys(value)

    def enter_address(self, value):
        self.address.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def enter_password_confirm(self, value):
        self.password_confirm.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def get_error_message_name_error(self):
        return self.driver.find_element(*RegLocators.REG_NAME_ERROR_MESSAGE).text



