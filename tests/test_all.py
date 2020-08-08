from typing import List, Any, TypeVar, Callable
import json

import sorting
from sorting.quick import middle_pivot, first_pivot, last_pivot

T = TypeVar("T")


def auto(sort_cb: Callable, test_data) -> None:
    data: List[T]
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


def test_sorting_algorithms():
    test_data: List[List[Any]] = json.load(open("tests/input.json"))
    for sort_cb in sorting.__all__:
        auto(getattr(sorting, sort_cb), test_data)


def test_pivot():
    assert last_pivot(0, 0) == 0
    assert last_pivot(0, 1) == 1
    assert first_pivot(0, 0) == 0
    assert first_pivot(0, 1) == 0
    assert first_pivot(0, 10) == 0
    assert middle_pivot(0, 0) == 0
    assert middle_pivot(0, 5) == 2
    assert middle_pivot(0, 6) == 3
