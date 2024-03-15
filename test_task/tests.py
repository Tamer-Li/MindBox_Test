import unittest
from calculate_figures import calculation


class TestTask(unittest.TestCase):
    """
    Тест на вычисление площади фигур
    """

    def test_area_calculation(self):
        """
        Здесь только правильные фигуры
        """

        data_for_test = {
            # Для Окружности
            (2, ): 12.566370614359172,
            (3, ): 28.274333882308138,
            (4, ): 50.26548245743669,
            (5, ): 78.53981633974483,
            (6, ): 113.09733552923255,

            # Для прямоугольника
            (2, 5, ): 10,
            (3, 6, ): 18,
            (4, 7, ): 28,
            (5, 8, ): 40,
            (6, 9, ): 54,

            # Для треугольника
            (7, 24, 25, ): 84,
            (7, 15, 20, ): 42,
            (9, 12, 15, ): 54,
            (10, 21, 23, ): 104.95713410721541,
            (11, 60, 61, ): 330,
        }

        for sides, result in data_for_test.items():
            self.assertEqual(calculation.area(*sides), result)

    def test_unknown_figures(self):
        """
        Тест на неизвестные фигуры
        """

        data_for_test_unknown_figures = [
            (8, 15, 17, 20, ),
            (12, 16, 20, 28, 32, ),
            (6, 8, 9, 12, 15, ),
            (4, 4, 7, 8, 10, ),
            (10, 12, 18, 20, 22, )
        ]

        for sides in data_for_test_unknown_figures:
            with self.assertRaises(NotImplementedError):
                calculation.area(*sides)

    def test_triangle_is_true(self):
        """
        Тест на правильность треугольника по сторонам
        Здесь только неправильные треугольники
        """
        data_for_false_triangle = [
            (1, 2, 3, ),
            (10, 11, 23, ),
            (8, 6, 2, ),
            (5, 4, 1, ),
            (10, 3, 6, )
        ]
        for sides in data_for_false_triangle:
            with self.assertRaises(ValueError):
                calculation.area(*sides)

    def test_triangle_is_right(self):
        """
        Тест на прямоугольного треугольника
        """
        data_for_test = {
            (3, 4, 5, ): True,
            (5, 12, 13, ): True,
            (2, 3, 4, ): False,
            (8, 15, 17, ): True,
            (4, 5, 6, ): False,
        }

        for sides, result in data_for_test.items():
            self.assertEqual(
                calculation.Triangle(*sides).triangle_is_right(), result
            )

    def test_triangle_is_isosceles(self):
        """
        Тест на равнобедренного треугольника
        """
        data_for_test = {
            (2, 2, 3, ): True,
            (3, 4, 5, ): False,
            (10, 10, 19, ): True,
            (4, 5, 6, ): False,
            (8, 8, 10, ): True,
        }

        for sides, result in data_for_test.items():
            self.assertEqual(
                calculation.Triangle(*sides).triangle_is_isosceles(), result
            )

    def test_triangle_is_equilateral(self):
        """
        Тест на равностороннего треугольника
        """
        data_for_test = {
            (1, 1, 1, ): True,
            (2, 1, 2, ): False,
            (5, 5, 5, ): True,
            (6, 5, 6, ): False,
            (10, 10, 10, ): True,
        }

        for sides, result in data_for_test.items():
            self.assertEqual(
                calculation.Triangle(*sides).triangle_is_equilateral(), result
            )

    def test_rectangle_is_square(self):
        """
        Является ли прямоугольник - квадратом
        """
        data_for_test = {
            (2, 2, ): True,
            (5, 3, ): False,
            (7, 7, ): True,
            (1, 4, ): False,
            (6, 6, ): True,
        }

        for sides, result in data_for_test.items():
            self.assertEqual(
                calculation.Rectangle(*sides).rectangle_is_square(), result
            )


if __name__ == '__main__':
    unittest.main()
