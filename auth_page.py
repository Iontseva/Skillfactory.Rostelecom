from locators import AuthLocators
from base_page import BasePage
from selenium.webdriver.support.color import Color


class AuthPage(BasePage):
    def __init__(self, driver,timeout=3):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/"
        driver.get(url)
        #создаем нужные элементы
        self.tab_phone = driver.find_element(*AuthLocators.AUTH_TAB_PHONE)
        self.tab_mail = driver.find_element(*AuthLocators.AUTH_TAB_MAIL)
        self.tab_login = driver.find_element(*AuthLocators.AUTH_TAB_LOGIN)
        self.tab_ls = driver.find_element(*AuthLocators.AUTH_TAB_LS)
        self.username = driver.find_element(*AuthLocators.AUTH_USERNAME)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)

    # Описываем функции для элементов страницы
    def click_tab_phone(self):
        self.tab_phone.click()

    def click_tab_mail(self):
        self.tab_mail.click()

    def click_tab_login(self):
        self.tab_login.click()

    def click_tab_ls(self):
        self.tab_ls.click()

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def get_error_message(self):
        return self.driver.find_element(*AuthLocators.AUTH_WRONG_LOGIN_OR_PASSWORD).text

    def get_forgot_password_color(self):
        rgb = self.driver.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD).value_of_css_property('color')
        return Color.from_string(rgb).hex

