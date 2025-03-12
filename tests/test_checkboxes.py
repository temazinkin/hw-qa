from itertools import combinations

import pytest

from pages.checkboxes_page import CheckboxesPage


@pytest.mark.parametrize('indexes', [
    *combinations(range(3), 1),
    *combinations(range(3), 2),
    *combinations(range(3), 3),
])
def test_checkboxes(driver, indexes):
    page = CheckboxesPage(driver)
    texts = page.click_by_index(indexes)
    page.submit()
    assert page.result_text == ', '.join(texts).lower()
