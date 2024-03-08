"""
Quick sort using recursion
"""
import random
from typing import List


def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


if __name__ == "__main__":
    arr1 = [10, 7, 8, 9, 1, 5]
    size = len(arr1)
    quicksort(arr1, 0, high=(size - 1))
    print(f"After sorting array: {arr1}")
