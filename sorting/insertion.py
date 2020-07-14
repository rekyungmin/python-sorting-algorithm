__all__ = ("insertion_sort",)

from typing import List, TypeVar

T = TypeVar("T")


def insertion_sort(
    data: List[T], *, reverse: bool = False, inplace: bool = False
) -> List[T]:
    if not inplace:
        data = data.copy()

    comparison_op: str = "__lt__" if reverse else "__gt__"
    max_len: int = len(data)

    for i in range(1, max_len):
        selected: T = data[i]
        j: int = i
        while j > 0 and getattr(data[j - 1], comparison_op)(selected):
            data[j] = data[j - 1]  # move right
            j -= 1

        data[j] = selected

    return data
