import random
import time

from sorts import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    shell_sort,
    merge_sort,
    quick_sort,
    heap_sort,
    radix_sort,
)

SORT_FUNCTIONS = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Shell Sort": shell_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
    "Radix Sort": radix_sort,
}

def generate_list(
    size: int, 
    order: str
) -> list:
    """
    Generate a list of random integers.
    """
    arr = [random.randint(0, size * 10) for _ in range(size)]

    if order == "Ordenada":
        return sorted(arr)

    elif order == "Invertida":
        return sorted(arr, reverse=True)

    else:
        return arr


def run_sort(
    sort_func: callable, 
    arr: list
) -> tuple[list, float]:
    """
    Run the sorting function and return the sorted list and time taken.
    """
    arr_copy = arr.copy()
    start = time.perf_counter()
    sorted_arr = sort_func(arr_copy)
    end = time.perf_counter()
    return sorted_arr, end - start