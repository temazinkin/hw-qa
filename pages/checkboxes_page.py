from pages.base_page import SubmitPage


class CheckboxesBasePage(SubmitPage):
    CHECKBOX_SELECTOR = '.form-check-inline'

    def _checkboxes(self):
        return self.find_elements(self.CHECKBOX_SELECTOR)

    def click_by_index(self, indexes):
        checkboxes = self._checkboxes()
        texts = []
        for index, checkbox in enumerate(checkboxes):
            if index in indexes:
                checkbox.click()
                texts.append(checkbox.text)
        return texts


class SingleCheckboxPage(CheckboxesBasePage):
    # TODO: SingleCheckboxPage
    ...


class CheckboxesPage(CheckboxesBasePage):
    URL = 'https://www.qa-practice.com/elements/checkbox/mult_checkbox'
