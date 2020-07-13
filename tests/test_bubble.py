from sorting.bubble import bubble_sort, bubble_sort_imp
from tests.auto_test import auto


def test_bubble() -> None:
    auto(bubble_sort)
    auto(bubble_sort_imp)
