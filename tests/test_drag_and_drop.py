from pages.drag_and_drop import DragAndDropPage


def test_drag_and_drop(driver):
    page = DragAndDropPage(driver)
    page.drag_and_drop()
    assert page.result_text == 'Dropped!'


# TODO: Images, drag-and-drop
