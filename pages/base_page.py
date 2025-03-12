from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    URL = None
    TIMEOUT = 5
    RESULT_SELECTOR = '#result-text'

    @property
    def result_text(self):
        return self.find_element(self.RESULT_SELECTOR).text

    def __init__(self, driver):
        self.driver = driver
        self._open()

    def _open(self):
        if self.URL is not None:
            self.driver.get(self.URL)

    def _wait_element(self, css_selector):
        wait = WebDriverWait(self.driver, self.TIMEOUT)
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, css_selector)
        ))

    def wait_contains_class(self, css_selector, class_name):
        wait = WebDriverWait(self.driver, self.TIMEOUT)
        wait.until(EC.text_to_be_present_in_element_attribute(
            (By.CSS_SELECTOR, css_selector),
            'class', class_name
        ))

    def find_element(self, css_selector):
        self._wait_element(css_selector)
        return self.driver.find_element(
            By.CSS_SELECTOR, css_selector
        )

    def find_elements(self, css_selector):
        self._wait_element(css_selector)
        return self.driver.find_elements(
            By.CSS_SELECTOR, css_selector
        )


class SubmitPage(BasePage):
    SUBMIT_BUTTON = '#submit-id-submit'

    def submit(self):
        self.find_element(self.SUBMIT_BUTTON).click()
