from typing import List, Any, TypeVar, Callable
import json

import sorting

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


def test_all():
    test_data: List[List[Any]] = json.load(open("tests/input.json"))
    for sort_cb in sorting.__all__:
        auto(getattr(sorting, sort_cb), test_data)
