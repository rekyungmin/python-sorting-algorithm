from sorting.selection import selection_sort
from tests.auto_test import auto


def test_selection() -> None:
    auto(selection_sort)
