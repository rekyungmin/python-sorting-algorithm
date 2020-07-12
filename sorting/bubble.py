from typing import List, TypeVar

__all__ = (
    "bubble_sort",
)

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
