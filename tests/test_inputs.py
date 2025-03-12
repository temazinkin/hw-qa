import pytest

from pages.inputs_page import (
    SimpleInputPage,
    EmailInputPage,
)


@pytest.mark.simple_input
@pytest.mark.parametrize('text', [
    'helloworld',
    'Hello_World',
    'Hello-World',
    '123789',
    'Hello_1-23',
])
def test_simple_success(driver, text):
    page = SimpleInputPage(driver)
    page.send_text(text)
    page.press_enter()
    assert page.result_text == text


@pytest.mark.simple_input
@pytest.mark.parametrize('text, error', [
    ('привет', 'Enter a valid string consisting of letters, numbers, underscores or hyphens.'),
    ('d', 'Please enter 2 or more characters'),
    ('d' * 50, 'Please enter no more than 25 characters'),
])
def test_simple_error(driver, text, error):
    page = SimpleInputPage(driver)
    page.send_text(text)
    page.press_enter()
    assert page.is_invalid_input
    assert page.feedback == error


@pytest.mark.email_input
@pytest.mark.parametrize('email', [
    'test@example.com',
    'demo@localhost',
])
def test_email_success(driver, email):
    page = EmailInputPage(driver)
    page.send_text(email)
    page.press_enter()
    assert page.result_text == email


@pytest.mark.email_input
@pytest.mark.parametrize('email', [
    'example.com',
    'demo@anydomain',
])
def test_email_error(driver, email):
    page = EmailInputPage(driver)
    page.send_text(email)
    page.press_enter()
    assert page.is_invalid_input
    assert page.feedback == 'Enter a valid email address.'


# TODO: Password Input
