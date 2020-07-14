__all__ = ("selection_sort",)

from typing import List, TypeVar

T = TypeVar("T")


def selection_sort(
    data: List[T], *, reverse: bool = False, inplace: bool = False
) -> List[T]:
    if not inplace:
        data = data.copy()

    comparison_op: str = "__lt__" if reverse else "__gt__"
    max_len: int = len(data)

    for i in range(max_len - 1):
        # find the min or max index
        minmax_index: int = i
        for j in range(i + 1, max_len):
            if getattr(data[minmax_index], comparison_op)(data[j]):
                minmax_index = j

        data[i], data[minmax_index] = data[minmax_index], data[i]

    return data
