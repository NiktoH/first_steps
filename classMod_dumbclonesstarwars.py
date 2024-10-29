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

    def volume(self) -> Union[int, float]:
        pass


class Rectangle(Shape):
    _count: int = 0

    def __init__(self, width: Union[int, float],
                 height: Union[int, float]):
        self._width: Union[int, float] = width
        self._height: Union[int, float] = height
        Rectangle._count += 1

    @staticmethod
    def get_count() -> int:
        return Rectangle._count

    def area(self) -> Union[int, float]:
        return self._width * self._height

    def perimetr(self) -> Union[int, float]:
        return 2 * (self._width + self._height)


class ThirdDimensionRectangle(Shape):
    def __init__(self, width: Union[int, float],
                height: Union[int, float],
                length: Union[int, float]):
        self._width: Union[int, float] = width
        self._height: Union[int, float] = height
        self._length: Union[int, float] = length

    def area(self) -> Union[int, float]:
        return 2 * (self._width * self._height + self._height * self._length + self._width * self._length)

    def perimetr(self) -> Union[int, float]:
        return 2 * (self._width + self._height)

    @property
    def volume(self):
        return self._length * self._width * self._height


r = ThirdDimensionRectangle(10, 10, 10)


class Square(Rectangle):
    def __init__(self, side: Union[int, float]):
        super().__init__(side, side)



class Circle(Shape):
    _count: int = 0

    def __init__(self, radius: Union[int, float]):
        self._radius = radius
        Circle._count += 1

    @staticmethod
    def get_count() -> int:
        return Circle._count

    def area(self):
        return math.pi * (self._radius ** 2)

    def perimetr(self):
        return 2 * math.pi * self._radius


if __name__ == "__main__":
    shapes = [
        Rectangle(3, 4),
        Square(3),
        Circle(2),
        Rectangle(6, 7),
        ThirdDimensionRectangle(10, 10, 10)
    ]


    for shape in shapes:
        print(f"Фигура: {type(shape).__name__}, Площадь: {shape.area()}, Периметр: {shape.perimetr()}")


    print(f"Всего прямоугольников: {Rectangle.get_count()}")
    print(f"Всего кругов: {Circle.get_count()}")
    print(f"Объём параллепипеда: {r.volume}")
