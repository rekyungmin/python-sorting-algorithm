__all__ = (
    "bubble_sort",
    "bubble_sort_imp",
)

from typing import List, TypeVar

T = TypeVar("T")


def bubble_sort(
    data: List[T], *, reverse: bool = False, inplace: bool = False
) -> List[T]:
    if not inplace:
        data = data.copy()

    comparison_op: str = "__lt__" if reverse else "__gt__"
    max_len: int = len(data)
    for i in range(max_len):
        is_compare: bool = False
        for j in range(max_len - i - 1):
            if getattr(data[j], comparison_op)(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
                is_compare = True
        if not is_compare:
            break
    return data


def bubble_sort_imp(
    data: List[T], *, reverse: bool = False, inplace: bool = False
) -> List[T]:
    if not inplace:
        data = data.copy()

    comparison_op: str = "__lt__" if reverse else "__gt__"
    unsorted_max_index: int = len(data) - 1
    last_unsorted_max_index: int = -1

    while unsorted_max_index != last_unsorted_max_index:
        last_unsorted_max_index = unsorted_max_index
        for i in range(unsorted_max_index):
            if getattr(data[i], comparison_op)(data[i + 1]):
                data[i], data[i + 1] = data[i + 1], data[i]
                unsorted_max_index = i
    return data
