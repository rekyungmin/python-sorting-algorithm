__all__ = ("merge_sort",)

from typing import List, TypeVar

T = TypeVar("T")


def merge_sort(
    data: List[T], *, reverse: bool = False, inplace: bool = False
) -> List[T]:
    if not inplace:
        data = data.copy()

    comparison_op: str = "__lt__" if reverse else "__gt__"
    _merge_sort(data, comparison_op)
    return data


def _merge_sort(data: List[T], comparison: str) -> None:
    if len(data) <= 1:
        return

    mid: int = len(data) // 2
    left_part: List[T] = data[:mid]
    right_part: List[T] = data[mid:]

    _merge_sort(left_part, comparison)
    _merge_sort(right_part, comparison)

    right_i = left_i = i = 0

    while True:
        if getattr(left_part[left_i], comparison)(right_part[right_i]):
            data[i] = right_part[right_i]
            right_i += 1
            if right_i == len(right_part):
                data[i + 1 :] = left_part[left_i:]
                break
        else:
            data[i] = left_part[left_i]
            left_i += 1
            if left_i == len(left_part):
                data[i + 1 :] = right_part[right_i:]
                break
        i += 1
