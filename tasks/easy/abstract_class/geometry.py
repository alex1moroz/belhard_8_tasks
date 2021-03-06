"""
Описать абстрактный класс Shape - фигура, у которого:

- абстрактный метод get_perimeter (не принимает аргументов) для расчета периметра
- абстрактный метод get_square (не принимает аргументов) для расчета площади

Во всех дочерних классах методы get_perimeter и get_square должны возвращать
результат вычислений.

Описать класс Circle для круга (дочерний класс для Shape), у которого:

- атрибут r - радиус, тип float
- магический метод __init__, который принимает r
- перегрузить метод get_perimeter (формула длины окружности: 2 * pi * r)
- перегрузить метод get_square (формула площади: pi * r ** 2)

Описать класс Rectangle для прямоугольника (дочерний класс для Shape), у которого:

- атрибут a - первая сторона, тип float
- атрибут b - вторая сторона, тип float
- магический метод __init__, который принимает a и b
- перегрузить метод get_perimeter (формула периметра: 2 * (a + b))
- перегрузить метод get_square (формула площади: a * b)

Описать класс Square для квадрата (дочерний класс для Rectangle), у которого:

- магический метод __init__, который принимает a, вызывает super
"""
from abc import ABC, abstractmethod
from math import pi
