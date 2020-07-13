<h1 align="center">Sorting algorithm</h1>
<p align="center">
<a href ="https://travis-ci.com/rekyungmin/python-sorting-algorithm"><img alt="Build status" src="https://travis-ci.com/rekyungmin/python-sorting-algorithm.svg?branch=master"></a>
<a href='https://coveralls.io/github/rekyungmin/python-sorting-algorithm?branch=master'><img src='https://coveralls.io/repos/github/rekyungmin/python-sorting-algorithm/badge.svg?branch=master' alt='Coverage Status' /></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Bubble sort
```python
bubble_sort(data: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]
bubble_sort_imp(data: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]
```

| Best | Average | Worst | Memory(~In place) | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| <i>n</i>  | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620"> | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620"> | 1 (In-place)      | Yes    | Exchanging |


```python
>>> data = [1, 5, 3, 2, 1, 10, 8, 25, 22, 48, 7]
>>> print(bubble_sort(data))
[1, 1, 2, 3, 5, 7, 8, 10, 22, 25, 48]
>>> print(bubble_sort(data, reverse=True))
[48, 25, 22, 10, 8, 7, 5, 3, 2, 1, 1]
>>> bubble_sort(data, reverse=True, inplace=True)
>>> data
[48, 25, 22, 10, 8, 7, 5, 3, 2, 1, 1]
```

## Selection sort
```python
selection_sort(data: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]
```

| Best | Average | Worst | Memory(~In place) | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">  | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">   | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620"> | 1 (In-place)      | **No**    | Insertion |
