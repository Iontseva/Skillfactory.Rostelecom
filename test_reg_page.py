from reg_page import RegPage
import pytest
from parametrize import *

timeout = 20

@pytest.mark.parametrize('name',
                         [generate_string(2),
                          generate_string(3),
                          generate_string(29),
                          generate_string(30)])
@pytest.mark.parametrize('lastname',
                         [generate_string(2),
                          generate_string(3),
                          generate_string(29),
                          generate_string(30)])
@pytest.mark.parametrize('address',
                         ['example@email.ru',
                          '+79999999999',
                          '+375999999999'])
def test_reg_page_add_name_correct(selenium, name, lastname, address):
    """Позитивный тест на проверку страницы регистрации при корректно ввдённых данных"""
    page = RegPage(selenium, timeout)
    page.enter_name(name)
    page.enter_lastname(lastname)
    page.enter_address('test@mail.ru')
    page.enter_password('61dBzx@o')
    page.enter_password_confirm('61dBzx@o')
    page.btn_click()

    assert page.get_redirect_uri_link() == '/auth/realms/b2c/login-actions/registration'




@pytest.mark.parametrize('name',
                         [generate_string(0),
                          generate_string(1),
                          generate_string(31),
                          generate_string(255),
                          generate_string(1001),
                          english_chars(),
                          special_chars(),
                          '12345',
                          ])
def test_reg_page_add_name_incorrect(selenium, name):
    """Негативный тест на проверку поля 'Имя' при некорректно ввдённых данных"""
    page = RegPage(selenium, timeout)
    page.enter_name(name)
    page.btn_click()

    assert page.get_error_message_name_error() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

@pytest.mark.parametrize('lastname',
                         [generate_string(0),
                          generate_string(1),
                          generate_string(31),
                          generate_string(255),
                          generate_string(1001),
                          english_chars(),
                          special_chars(),
                          '12345',
                          ''])
def test_reg_page_add_lastname_incorrect(selenium, lastname):
    """Негативный тест на проверку поля 'Фамилия' при некорректно введённых данных"""
    page = RegPage(selenium, timeout)
    page.enter_lastname(lastname)
    page.btn_click()
    assert page.get_error_message_name_error() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'



