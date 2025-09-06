# Задание 8: Функции
# Реализуйте различные функции согласно их описанию


def greet(name):
    """
    Возвращает приветствие для имени
    Например, "Привет, Иван!"
    """
    # Ваш код здесь
    return f"Привет, {name}!"


def absolute_value(number):
    """
    Возвращает абсолютное значение числа
    """
    # Ваш код здесь
    return abs(number)


def calculate_area(shape, *args):
    """
    Вычисляет площадь фигуры

    Параметры:
    - shape: строка, тип фигуры ("circle", "rectangle", "triangle")
    - *args: аргументы для вычисления площади
        - для "circle": радиус
        - для "rectangle": длина и ширина
        - для "triangle": основание и высота

    Возвращает:
    - площадь фигуры или None, если тип фигуры неизвестен
    """
    # Ваш код здесь
    import math

    match shape:
        case "circle": return math.pi * args[0]**2
        case "rectangle": return math.prod(args)
        case "triangle": return math.prod(args) / 2
        case _: return None


def apply_operation(operation, a, b):
    """
    Применяет операцию к двум числам

    Параметры:
    - operation: строка, операция ("add", "subtract", "multiply", "divide")
    - a, b: числа

    Возвращает:
    - результат операции или None, если операция неизвестна
    """
    # Ваш код здесь
    match operation:
        case "add": return a + b
        case "subtract": return a - b
        case "multiply": return a * b
        case "divide": return None if b == 0 else a / b
        case _: return None


def create_multiplier(factor):
    """
    Создает и возвращает функцию, которая умножает свой аргумент на factor

    Пример использования:
    double = create_multiplier(2)
    result = double(5)  # result = 10
    """
    # Ваш код здесь
    return lambda x: x * factor


def apply_to_each(func, items):
    """
    Применяет функцию func к каждому элементу списка items
    и возвращает список результатов

    Пример использования:
    result = apply_to_each(lambda x: x*2, [1, 2, 3])  # result = [2, 4, 6]
    """
    # Ваш код здесь
    return [func(i) for i in items]
