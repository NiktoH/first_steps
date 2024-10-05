from abc import ABC, abstractmethod

#Абстрактный класс

class Shape(ABC):
    @abstractmethod
    def area(self) -> any:
        pass

    @abstractmethod
    def perimetr(self) -> any:
        pass

#Класс прямоугольника
class Rectangle(Shape):
    #Кол-во прямоугольников
    _count: int = 0

    def __init__(self, width: any, height: any):
        self._width = width
        self._height = height
        Rectangle._count += 1

    @staticmethod
    def get_count() -> int:
        return Rectangle._count

    def area(self) -> any:
        return self._width * self._height

    def perimetr(self) -> any:
        return 2 * (self._width + self._height)

#Класс квадрата и конструктор родительского класса
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

#Класс круга
class Circle(Shape):
    _count: int = 0

    def __init__(self, radius: any):
        self._radius = radius
        Circle._count += 1

    @staticmethod
    def get_count():
        return Circle._count

    def area(self):
        return 3.14 * (self._radius ** 2)

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
