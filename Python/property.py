class Point:
    dimension = 2

    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        self._y = y


if __name__ == "__main__":
    point = Point(1, 2)
    print("Point:", point)

    setattr(Point, "z", 100)
    print("Point-z:", point.z)

    setattr(Point, "distance", property(lambda self: (self.x**2 + self.y**2) ** 0.5))
    print("Point-distance:", point.distance)
