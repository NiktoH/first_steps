import math

from typing import Union
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> Union[int, float]:
        pass

    @abstractmethod
    def perimetr(self) -> Union[int, float]:
        pass


class Rectangle(Shape):
    _count: int = 0

    def __init__(self, width: Union[int, float],
                 height: Union[int, float]):
        self._width: Union[int, float] = width
        self._height: Union[int, float] = height
        Rectangle._count += 1

    @staticmethod
    def get_count(self) -> int:
        return Rectangle._count

    def area(self) -> Union[int, float]:
        return self._width * self._height

    def perimetr(self) -> Union[int, float]:
        return 2 * (self._width + self._height)

    count = property(get_count)
    sarea = property(area)
    sperimetr = property(perimetr)


class Square(Rectangle):
    def __init__(self, side: Union[int, float]):
        super().__init__(side, side)


class Circle(Shape):
    _count: int = 0

    def __init__(self, radius: Union[int, float]):
        self._radius = radius
        Circle._count += 1

    @staticmethod
    def get_count(self):
        return Circle._count

    def area(self):
        return math.pi * (self._radius ** 2)

    def perimetr(self):
        return 2 * math.pi * self._radius

    count = property(get_count)
    sarea = property(area)
    sperimetr = property(perimetr)


if __name__ == "__main__":
    shapes = [
        Rectangle(3, 4),
        Square(3),
        Circle(2),
        Rectangle(6, 7)
    ]


    for shape in shapes:
        print(f"Фигура: {type(shape).__name__}, Площадь: {shape.sarea}, Периметр: {shape.sperimetr}")


    print(f"Всего прямоугольников: {shape.count}")
    print(f"Всего кругов: {shape.count}")
