from operator import gt, lt
from random import randint


class Heap:
    def __init__(self, max_heap: bool = True) -> None:
        self._heap: list[int] = [0]
        self.max_heap = max_heap
        self._operation = gt if max_heap else lt

    def __len__(self) -> int:
        return len(self._heap) - 1

    def compare(self, child_idx: int) -> bool:
        return self._heap[child_idx] == self._heap[child_idx // 2] or self._operation(
            self._heap[child_idx // 2], self._heap[child_idx]
        )

    def _push_heapify(self) -> None:
        idx = len(self._heap) - 1
        while idx > 1:
            parent_idx = idx // 2
            if not self.compare(idx):
                self._heap[parent_idx], self._heap[idx] = (
                    self._heap[idx],
                    self._heap[parent_idx],
                )
                idx //= 2
            else:
                break

    def _pop_heapify(self) -> None:
        idx = 1
        while idx < len(self._heap):
            left_child_idx = idx * 2
            right_child_idx = idx * 2 + 1
            left_child = True
            if left_child_idx >= len(self._heap):
                break

            if right_child_idx == len(self._heap):
                child_idx = left_child_idx
            elif self._heap[left_child_idx] > self._heap[right_child_idx]:
                child_idx = left_child_idx
            else:
                child_idx = right_child_idx
                left_child = False
            if not self.compare(child_idx):
                self._heap[idx], self._heap[child_idx] = (
                    self._heap[child_idx],
                    self._heap[idx],
                )
                idx *= 2
                if not left_child:
                    idx += 1
            else:
                break

    def push(self, x: int) -> None:
        self._heap.append(x)
        self._push_heapify()

    def pop(self) -> int:
        num = self._heap[1]
        self._heap[1] = self._heap[-1]
        self._heap.pop()
        self._pop_heapify()
        return num


def verify_heap(heap: Heap) -> bool:
    heap_len = len(heap)
    if not heap_len:
        return True

    last_idx = heap_len + 1

    for i in range(1, last_idx):
        left, right = i * 2, i * 2 + 1
        try:
            if not heap.compare(left):
                return False
            if not heap.compare(right):
                return False
        except IndexError:
            pass
    return True


def test_heap() -> None:
    heap = Heap()

    for _ in range(10_000):
        heap.push(randint(1, 100_000))
        if not verify_heap(heap):
            raise Exception("Validation not passed")
    for _ in range(10_000):
        heap.pop()
        verify_heap(heap)
        if not verify_heap(heap):
            raise Exception("Validation not passed")


if __name__ == "__main__":
    heap = Heap()

    for x in [2, 6, 3, 8, 1, 9]:
        heap.push(x)
        print(heap._heap)

    for _ in range(6):
        print(heap.pop())
        print(heap._heap)

    test_heap()
