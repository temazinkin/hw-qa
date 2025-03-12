from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class DragAndDropBasePage(BasePage):
    DROP_SELECTOR = '#rect-droppable'
    DRAG_SELECTOR = '#rect-draggable'
    RESULT_SELECTOR = '#text-droppable'

    def _drag(self):
        return self.find_element(self.DRAG_SELECTOR)

    def _drop(self):
        return self.find_element(self.DROP_SELECTOR)

    def drag_and_drop(self):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(self._drag(), self._drop()).perform()


class DragAndDropPage(DragAndDropBasePage):
    URL = 'https://www.qa-practice.com/elements/dragndrop/boxes'


class ImageDropPage(DragAndDropBasePage):
    # TODO: Images, drag-and-drop
    ...
