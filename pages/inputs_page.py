from selenium.webdriver import Keys

from pages.base_page import BasePage


class InputBasePage(BasePage):
    INPUT_SELECTOR = None
    INVALID_INPUT_CLASS = 'is-invalid'
    FEEDBACK_SELECTOR = '.invalid-feedback'

    @property
    def feedback(self):
        return self.find_element(self.FEEDBACK_SELECTOR).text

    @property
    def is_invalid_input(self):
        self.wait_contains_class(
            self.INPUT_SELECTOR, self.INVALID_INPUT_CLASS
        )
        class_list = self._input().get_attribute('class').split()
        return self.INVALID_INPUT_CLASS in class_list

    def _input(self):
        return self.find_element(self.INPUT_SELECTOR)

    def send_text(self, text):
        self._input().send_keys(text)

    def press_enter(self):
        self._input().send_keys(Keys.ENTER)


class SimpleInputPage(InputBasePage):
    URL = 'https://www.qa-practice.com/elements/input/simple'
    INPUT_SELECTOR = '#id_text_string'


class EmailInputPage(InputBasePage):
    URL = 'https://www.qa-practice.com/elements/input/email'
    INPUT_SELECTOR = '#id_email'

# TODO: Password Input
