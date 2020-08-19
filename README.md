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
>>> bubble_sort(data)
[1, 1, 2, 3, 5, 7, 8, 10, 22, 25, 48]
>>> bubble_sort(data, reverse=True)
[48, 25, 22, 10, 8, 7, 5, 3, 2, 1, 1]
>>> data
[1, 5, 3, 2, 1, 10, 8, 25, 22, 48, 7]
>>> bubble_sort(data, reverse=True, inplace=True)
[48, 25, 22, 10, 8, 7, 5, 3, 2, 1, 1]
>>> data
[48, 25, 22, 10, 8, 7, 5, 3, 2, 1, 1]
```

## Selection sort
```python
selection_sort(data: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]
```

| Best | Average | Worst | Memory | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">  | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">   | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620"> | 1 (In-place)      | **No**    | Selection |

## Insertion sort
```python
insertion_sort(data: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]
```

| Best | Average | Worst | Memory | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">  | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">   | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620"> | 1 (In-place)      | Yes    | Insertion |

## Merge sort
```python
merge_sort(data: List[T], *, reverse: bool = False, inplace: bool = False) -> List[T]
```

| Best | Average | Worst | Memory | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/560dfdce0353a330e03e4b3e0b7ca6e484bb40fb">  | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/560dfdce0353a330e03e4b3e0b7ca6e484bb40fb">   | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/560dfdce0353a330e03e4b3e0b7ca6e484bb40fb"> | <i>n</i> (Not in-place)      | Yes    | Merging |

## Quick sort
```python
def quick_sort(
    data: List[T],
    *,
    reverse: bool = False,
    inplace: bool = False,
    pivot_cb: Callable[[int, int], int] = middle_pivot
) -> List[T]:
```

pivot_cb: `first_pivot`, `middle_pivot`(default), `last_pivot`

| Best | Average | Worst | Memory | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/560dfdce0353a330e03e4b3e0b7ca6e484bb40fb">  | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/560dfdce0353a330e03e4b3e0b7ca6e484bb40fb">   | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620"> | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/317ab5292da7c7935aec01a570461fe0613b21d5"> (worst case: <i>n</i>)      | **No** | Partitioning |

```python
>>> data = [1, 5, 3, 2, 1, 10, 8, 25, 22, 48, 7]
>>> quick_sort(data)
[1, 1, 2, 3, 5, 7, 8, 10, 22, 25, 48]
>>> quick_sort(data, pivot_cb=last_pivot)
[1, 1, 2, 3, 5, 7, 8, 10, 22, 25, 48]
>>> quick_sort(data, pivot_cb=first_pivot)
[1, 1, 2, 3, 5, 7, 8, 10, 22, 25, 48]
>>> quick_sort(data, reverse=True)
[48, 25, 22, 10, 8, 7, 5, 3, 2, 1, 1]
>>> data
[1, 5, 3, 2, 1, 10, 8, 25, 22, 48, 7]
>>> quick_sort(data, reverse=True, inplace=True)
[48, 25, 22, 10, 8, 7, 5, 3, 2, 1, 1]
>>> data
[48, 25, 22, 10, 8, 7, 5, 3, 2, 1, 1]
```