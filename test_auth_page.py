from auth_page import AuthPage
# Необходимые для теста данные хранятся в файле dataset
from dataset import *

timeout = 20

def test_auth_page_valid_phone_valid_pass(selenium):
    """Позитивный тест: валидный номер телефона, валидный пароль"""
    page = AuthPage(selenium, timeout)
    page.click_tab_phone()
    page.enter_username(valid_phone)
    page.enter_pass(valid_password)
    page.btn_click()

    assert page.get_redirect_uri_link() == '/account_b2c/page'

def test_auth_page_valid_email_valid_pass(selenium):
    """Позитивный тест: валидный email, валидный пароль"""
    page = AuthPage(selenium, timeout)
    page.click_tab_mail()
    page.enter_username(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()

    assert page.get_redirect_uri_link() == '/account_b2c/page'

def test_auth_page_valid_login_valid_pass(selenium):
    """Позитивный тест: валидный логин, валидный пароль"""
    page = AuthPage(selenium, timeout)
    page.click_tab_login()
    page.enter_username(valid_login)
    page.enter_pass(valid_password)
    page.btn_click()

    assert page.get_redirect_uri_link() == '/account_b2c/page'



def test_auth_page__valid_ls_valid_pass(selenium):
    """Позитивный тест: валидный номер лицевого счёта, валидный пароль"""
    page = AuthPage(selenium, timeout)
    page.click_tab_ls()
    page.enter_username(valid_ls)
    page.enter_pass(valid_password)
    page.btn_click()

    assert page.get_redirect_uri_link() == '/account_b2c/page'


def test_auth_page_valid_phone_invalid_pass(selenium):
    """Негативный тест: валидный номер телефона, невалидный пароль"""
    page = AuthPage(selenium, timeout)
    page.click_tab_phone()
    page.enter_username(valid_phone)
    page.enter_pass(invalid_password)
    page.btn_click()

    assert page.get_error_message() == 'Неверный логин или пароль'
    assert page.get_forgot_password_color() == '#ff4f12'

