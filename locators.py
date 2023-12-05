from selenium.webdriver.common.by import By

class AuthLocators:
    # класс локаторов элементов страницы аутентификации
    AUTH_USERNAME = (By.ID, 'username')
    AUTH_PASS = (By.ID, 'password')
    AUTH_BTN = (By.ID, 'kc-login')
    AUTH_TAB_PHONE = (By.ID, 't-btn-tab-phone')
    AUTH_TAB_MAIL = (By.ID, 't-btn-tab-mail')
    AUTH_TAB_LOGIN = (By.ID, 't-btn-tab-login')
    AUTH_TAB_LS = (By.ID, 't-btn-tab-ls')
    AUTH_WRONG_LOGIN_OR_PASSWORD = (By.ID, 'form-error-message')
    AUTH_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    AUTH_REGISTER = (By.ID, 'kc-register')

class RegLocators:
    # класс локаторов элементов страницы регистрации
    REG_NAME = (By.CSS_SELECTOR, 'input[name="firstName"]')
    REG_LASTNAME = (By.CSS_SELECTOR, 'input[name="lastName"]')
    REG_ADDRESS = (By.ID, 'address')
    REG_PASS = (By.ID, 'password')
    REG_PASS_CONF = (By.ID, 'password - confirm')
    REG_BTN = (By.NAME, "register")
    REG_NAME_ERROR_MESSAGE = (By.XPATH, '//div[@class = "name-container"]/div[1]/span')
    REG_LASTNAME_ERROR_MESSAGE = (By.XPATH, '//div[@class = "name-container"]/div[2]/span')

