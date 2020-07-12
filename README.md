# Sorting algorithm

## Bubble sort
| Best | Average | Worst | Memory(~In place) | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| $n$  | $n^2$   | $n^2$ | 1 (In-place)      | Yes    | Exchanging |

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
