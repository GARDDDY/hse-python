# Задание 6: Циклы (while)
# Реализуйте функции с использованием цикла while


def sum_of_digits(number):
    """
    Возвращает сумму цифр числа
    Например, для 123 результат должен быть 1 + 2 + 3 = 6
    """
    # Ваш код здесь
    return sum(map(int, str(number)))


def count_digits(number):
    """
    Возвращает количество цифр в числе
    Например, для 123 результат должен быть 3
    """
    # Ваш код здесь
    return len(str(number))


def reverse_number(number):
    """
    Возвращает число, записанное в обратном порядке
    Например, для 123 результат должен быть 321
    """
    # Ваш код здесь
    return int(str(number)[::-1])


def is_prime(number):
    """
    Проверяет, является ли число простым
    Простое число - это число больше 1, которое делится только на 1 и на само себя
    """
    # Ваш код здесь
    if number == 2:
        return True
    elif number <= 1 or number % 2 == 0:
        return False
    for i in range(3, int(number**0.5)+1, 2):
        if number % i == 0:
            return False
    return True


def gcd(a, b):
    """
    Находит наибольший общий делитель (НОД) двух чисел
    Используйте алгоритм Евклида
    """
    # Ваш код здесь
    while b != 0:
        a, b = b, a % b
    return a


def binary_search(sorted_list, target):
    """
    Реализует бинарный поиск элемента в отсортированном списке
    Возвращает индекс элемента, если он найден, иначе -1
    """
    # Ваш код здесь
    if target not in set(sorted_list):
        return -1

    l, r = 0, len(sorted_list)

    while l < r:
        m = (l+r)//2

        if sorted_list[m] < target:
            l = m + 1
        else:
            r = m

    return l
