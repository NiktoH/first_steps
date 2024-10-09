from abc import ABC, abstractmethod
from typing import Union
import math

#Абстрактный класс

class Shape(ABC):
    @abstractmethod
    def area(self) -> Union[int, float]:
        pass

    @abstractmethod
    def perimetr(self) -> Union[int, float]:
        pass

#Класс прямоугольника
class Rectangle(Shape):
    #Кол-во прямоугольников
    _count: int = 0

    def __init__(self, width: Union[int, float], height: Union[int, float]):
        self._width = width
        self._height = height
        Rectangle._count += 1

    @staticmethod
    def get_count() -> int:
        return Rectangle._count

    def area(self) -> Union[int, float]:
        return self._width * self._height

    def perimetr(self) -> Union[int, float]:
        return 2 * (self._width + self._height)

#Класс квадрата и конструктор родительского класса
class Square(Rectangle):
    def __init__(self, side: Union[int, float]):
        super().__init__(side, side)

#Класс круга
class Circle(Shape):
    _count: int = 0

    def __init__(self, radius: Union[int, float]):
        self._radius = radius
        Circle._count += 1

    @staticmethod
    def get_count():
        return Circle._count

    def area(self):
        return math.pi * (self._radius ** 2)

    def perimetr(self):
        return 2 * 3.14 * self._radius

if __name__ == "__main__":
    shapes = [
        Rectangle(3, 4),
        Square(3),
        Circle(2),
        Rectangle(6, 7)
    ]

    #Вывод информации о фигурах
    for shape in shapes:
        print(f"Фигура: {type(shape).__name__}, Площадь: {shape.area()}, Периметр: {shape.perimetr()}")

    print(f"Всего прямоугольников: {Rectangle.get_count()}")
    print(f"Всего кругов: {Circle.get_count()}")
