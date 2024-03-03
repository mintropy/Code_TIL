import time
from random import randint, shuffle


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took: {time.time() - start} seconds")
        return result

    return wrapper


@time_it
def bubble_sort(array: list, print_detail: bool = False) -> list:
    n = len(array)
    for i in range(n):
        if print_detail:
            print(array)
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    if print_detail:
        print(array)
    return array


if __name__ == "__main__":
    array1 = [i for i in range(10_000)]
    shuffle(array1)
    bubble_sort(array1)

    array2 = [randint(0, 100) for _ in range(5)]
    bubble_sort(array2, print_detail=True)
