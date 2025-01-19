import heapq


class Dijkstra:
    def __init__(self, graph: list[list[tuple[int, int]]], start_node: int = 0) -> None:
        self.graph = graph
        self.visited = [False] * len(graph)
        self.dist = [float("inf")] * len(graph)
        self.dist[start_node] = 0
        self.prev = [-1] * len(graph)
        self.queue: list[tuple[float | int, int]] = []

    def run(self, start_node: int = 0) -> None:
        self.queue.append((0, start_node))
        while self.queue:
            dist, node = heapq.heappop(self.queue)
            if self.visited[node]:
                continue
            self.visited[node] = True
            for neighbor, weight in self.graph[node]:
                if self.dist[neighbor] > dist + weight:
                    self.dist[neighbor] = dist + weight
                    self.prev[neighbor] = node
                    heapq.heappush(self.queue, (self.dist[neighbor], neighbor))

    def get_path(self, end) -> list[int]:
        path = []
        while end != -1:
            path.append(end)
            end = self.prev[end]
        return path[::-1]

    def get_distance(self, end) -> float | int:
        return self.dist[end]


if __name__ == "__main__":
    graph = [
        [(1, 4), (7, 8)],
        [(0, 4), (2, 8), (7, 11)],
        [(1, 8), (3, 7), (5, 4), (8, 2)],
        [(2, 7), (4, 9), (5, 14)],
        [(3, 9), (5, 10)],
        [(2, 4), (3, 14), (4, 10), (6, 2)],
        [(5, 2), (7, 1), (8, 6)],
        [(0, 8), (1, 11), (6, 1), (8, 7)],
        [(2, 2), (6, 6), (7, 7)],
    ]
    dijkstra = Dijkstra(graph)
    dijkstra.run()

    for i in range(len(graph)):
        print(f"Shortest path from 0 to {i}:", dijkstra.get_path(i))
        print(f"Shortest distance from 0 to {i}:", dijkstra.get_distance(i))
