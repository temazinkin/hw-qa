from pages.base_page import SubmitPage


class AlertBasePage(SubmitPage):
    SUBMIT_BUTTON = '#content > a.a-button'

    def _alert(self):
        return self.driver.switch_to.alert

    def alert_accept(self):
        self._alert().accept()

    def alert_reject(self):
        self._alert().dismiss()

    def alert_text(self, text):
        self._alert().send_keys(text)
        self._alert().accept()


class AlertPage(AlertBasePage):
    # TODO: Alert box
    ...


class ConfirmationPage(AlertBasePage):
    # TODO: Confirmation box
    ...


class PromptPage(AlertBasePage):
    URL = 'https://www.qa-practice.com/elements/alert/prompt'
