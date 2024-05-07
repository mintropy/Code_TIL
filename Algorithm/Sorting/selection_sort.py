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
def selection_sort(
    array: list, increasing: bool = True, print_detail: bool = False
) -> list:
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if increasing:
                if array[j] < array[min_index]:
                    min_index = j
            else:
                if array[j] > array[min_index]:
                    min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        if print_detail:
            print(array)
    if print_detail:
        print(array)
    return array


if __name__ == "__main__":
    array1 = [i for i in range(10_000)]
    shuffle(array1)
    selection_sort(array1)

    array2 = [randint(0, 100) for _ in range(5)]
    selection_sort(array2, print_detail=True)

    array3 = [randint(0, 100) for _ in range(5)]
    selection_sort(array3, increasing=False, print_detail=True)
