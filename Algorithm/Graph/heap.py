from operator import gt, lt


class Heap:
    def __init__(self, max_heap: bool = True) -> None:
        self._heap: list[int] = [0]
        self.max_heap = max_heap
        self._operation = lt if max_heap else gt

    def _push_heapify(self) -> None:
        idx = len(self._heap) - 1
        while idx > 1:
            parent_idx = idx // 2
            if self._operation(self._heap[parent_idx], self._heap[idx]):
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
            if self._operation(self._heap[idx], self._heap[child_idx]):
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


if __name__ == "__main__":
    heap = Heap()

    for x in [2, 6, 3, 8, 1, 9]:
        heap.push(x)
        print(heap._heap)

    for _ in range(6):
        print(heap.pop())
        print(heap._heap)
