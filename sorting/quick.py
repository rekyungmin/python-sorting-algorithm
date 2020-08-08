__all__ = (
    "quick_sort",
    "first_pivot",
    "middle_pivot",
    "last_pivot",
)

from typing import List, TypeVar, Callable

T = TypeVar("T")


def first_pivot(low: int, high: int) -> int:
    return low


def middle_pivot(low: int, high: int) -> int:
    return (low + high) // 2


def last_pivot(low: int, high: int) -> int:
    return high


def quick_sort(
    data: List[T],
    *,
    reverse: bool = False,
    inplace: bool = False,
    pivot_cb: Callable[[int, int], int] = middle_pivot
) -> List[T]:
    if not inplace:
        data = data.copy()

    comparison_op: str = "__lt__" if reverse else "__gt__"

    def sort(low: int, high: int) -> None:
        if low >= high:
            return

        mid: int = partition(low, high)
        sort(low, mid - 1)
        sort(mid + 1, high)

    def partition(low: int, high: int) -> int:
        pivot_index: int = pivot_cb(low, high)
        data[high], data[pivot_index] = data[pivot_index], data[high]
        pivot = data[high]
        left: int = low
        right: int = high - 1

        while True:
            while getattr(pivot, comparison_op)(data[left]) and left < right:
                left += 1
            while not getattr(pivot, comparison_op)(data[right]) and left < right:
                right -= 1
            if left >= right:
                break
            data[left], data[right] = data[right], data[left]

        if getattr(pivot, comparison_op)(data[left]):
            left += 1

        data[left], data[high] = data[high], data[left]
        return left

    sort(0, len(data) - 1)
    return data
