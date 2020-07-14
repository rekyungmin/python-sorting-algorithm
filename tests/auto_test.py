__all__ = ("auto",)

from typing import List, Tuple, TypeVar, Callable

T = TypeVar("T")


test_data: List[Tuple[T, T]] = [
    ([], []),
    ([1], [1]),
    ([-1], [-1]),
    ([1, 2], [1, 2]),
    ([-5, 1, -7, 10], [-7, -5, 1, 10]),
    ([1, 5, 3, 2, 1, 10, 8, 25, 22, 48, 7], [1, 1, 2, 3, 5, 7, 8, 10, 22, 25, 48]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
]


def auto(sort_cb: Callable) -> None:
    data: Tuple[T, T]
    for data in test_data:
        target: T = data[0].copy()
        assert sort_cb(target) == data[1]
        assert target == data[0]
        assert sort_cb(target, reverse=True) == list(reversed(data[1]))
        assert target == data[0]

        assert sort_cb(target, inplace=True) == data[1]
        assert target == data[1]
        if data[0] != data[1]:
            assert target != data[0]
