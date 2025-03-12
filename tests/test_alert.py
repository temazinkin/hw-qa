import pytest

from pages.alert_page import PromptPage


@pytest.fixture
def prompt_page(driver):
    page = PromptPage(driver)
    page.submit()
    return page


def test_alert():
    # TODO: Alert Box
    ...


def test_conformation():
    # TODO: Conformation box
    ...


def test_prompt_success(prompt_page):
    prompt_page.alert_text('Hello World!')
    assert prompt_page.result_text == 'Hello World!'


def test_prompt_empty(prompt_page):
    prompt_page.alert_accept()
    assert prompt_page.result_text == 'You entered nothing'


def test_prompt_decline(prompt_page):
    prompt_page.alert_reject()
    assert prompt_page.result_text == 'You canceled the prompt'
