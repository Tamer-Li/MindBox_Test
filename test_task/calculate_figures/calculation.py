# Напишите на C# или Python библиотеку для поставки внешним клиентам,
# которая умеет вычислять площадь круга по радиусу и треугольника по
# трем сторонам. Дополнительно к работоспособности оценим:
# - Юнит-тесты
# - Легкость добавления других фигур
# - Вычисление площади фигуры без знания типа фигуры в compile-time
# - Проверку на то, является ли треугольник прямоугольным

from math import sqrt, pi


class Figure:
    """
    Класс для создания базовой фигуры
    """

    def area(self):
        """
        Функция на определение метода 'area'.
        Ошибка 'NotImplementedError' подскажет,
        что именно нужно переопределить.
        """
        raise NotImplementedError(
            "Вы забыли переопределить метод 'area()'"
        )


class Circle(Figure):
    """
    Класс для окружности.

    Если при инициализации класса был принят один аргумент,
    то автоматически определяется радиус.
    """

    def __init__(
            self,
            radius: (int, float)
    ) -> None:
        self.radius = radius

    def area(self) -> (int, float):
        """
        Функция площади окружности
        :return: площадь (int, float)
        """
        return pi * (self.radius ** 2)


class Triangle(Figure):
    """
    Класс для треугольника

    Если при инициализации класса было принято три аргумента,
    то автоматически определяются три стороны треугольника.
    """

    def __init__(
            self,
            a: (int, float),
            b: (int, float),
            c: (int, float),
    ) -> None:

        # Проверка на существование такого треугольника
        if not (a + b > c and
                a + c > b and
                b + c > a):
            raise ValueError('Ошибка! Такой треугольник не может существовать')

        self.a = a
        self.b = b
        self.c = c

    def area(self) -> (int, float):
        """
        Функция для расчета площади треугольника по формуле Герона
        """

        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def triangle_is_right(self) -> bool:
        """
        Может ли треугольник быть прямоугольным
        :return: bool
        """

        # Так как мы точно не знаем в каком порядке вводились
        # стороны треугольника, то мы их записываем в список и
        # и сортируем по возрастанию. Это сделано для того,
        # чтобы удобно брать катеты и гипотенузу, ведь
        # гипотенуза больше катетов

        side_triangle = sorted([self.a, self.b, self.c])

        # Записываем квадраты сторон в отдельные переменные
        side_1_square = side_triangle[0] * side_triangle[0]
        side_2_square = side_triangle[1] * side_triangle[1]
        side_3_square = side_triangle[2] * side_triangle[2]

        # Проверка формулы Пифагора a**2 + b**c == c**2
        if side_1_square + side_2_square == side_3_square:
            return True

        return False

    def triangle_is_isosceles(self) -> bool:
        """
        Может ли треугольник быть равнобедренным (Личная разработка)
        :return: bool
        """

        if (
                self.a == self.b or
                self.b == self.c
                or self.c == self.a
        ):
            return True

        return False

    def triangle_is_equilateral(self) -> bool:
        """
        Может ли треугольник быть равносторонним (Лично от себя добавил)
        :return: bool
        """

        if self.a == self.b == self.c:
            return True

        return False


class Rectangle(Figure):
    """
    Класс для прямоугольника (Пример добавления фигуры)

    Если при инициализации класса было принято два аргумента,
    то автоматически определяются две стороны прямоугольника.
    """

    def __init__(
            self,
            length: (int, float),
            width: (int, float)
    ) -> None:
        self.length = length
        self.width = width

    def area(self) -> (int, float):
        return self.length * self.width

    def rectangle_is_square(self) -> bool:
        """
        Может ли прямоугольник быть квадратом
        :return: bool
        """

        if self.length == self.width:
            return True

        return False


def area(*args,):
    """
    Функция для тестов,
    проверяем кол-во входных аргументов в '*args'

    :param args: Входные данные
    :return: Выходные данные, либо ошибка
    """

    if len(args) == 1:
        return Circle(*args).area()

    if len(args) == 2:
        return Rectangle(*args).area()

    if len(args) == 3:
        return Triangle(*args).area()

    if len(args) > 3:
        raise NotImplementedError(
            "Пока нет реализации для таких аргументов"
        )


if __name__ == "__main__":
    pass
