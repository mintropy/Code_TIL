import time
from random import randint, shuffle


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(
            f"{func.__name__} took: {time.time() - start} seconds for {len(args[0])} elements"
        )
        return result

    return wrapper


@time_it
def insertion_sort(
    array: list, increasing: bool = True, print_detail: bool = False
) -> list:
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and (array[j] > key if increasing else array[j] < key):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        if print_detail:
            print(array)
    if print_detail:
        print(array)
    return array


if __name__ == "__main__":
    array1 = [i for i in range(10_000)]
    shuffle(array1)
    insertion_sort(array1)

    array2 = [randint(0, 100) for _ in range(5)]
    insertion_sort(array2, print_detail=True)

    array3 = [randint(0, 100) for _ in range(5)]
    insertion_sort(array3, increasing=False, print_detail=True)
