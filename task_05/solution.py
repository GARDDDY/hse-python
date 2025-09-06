# Задание 5: Циклы (for)
# Реализуйте функции с использованием цикла for


def sum_of_numbers(n):
    """
    Возвращает сумму чисел от 1 до n включительно
    """
    # Ваш код здесь
    return n * (n + 1) / 2


def factorial(n):
    """
    Возвращает факториал числа n (произведение чисел от 1 до n)
    Для n <= 1 возвращает 1
    """
    # Ваш код здесь
    return 1 if n < 2 else n*factorial(n-1)


def count_vowels(s):
    """
    Возвращает количество гласных букв в строке s
    Гласные: 'a', 'e', 'i', 'o', 'u' (регистр не имеет значения)
    """
    # Ваш код здесь
    import re

    return re.sub("[aeiouAEIOU]", "@", s).count("@")


def find_max(numbers):
    """
    Возвращает максимальное число из списка numbers
    Если список пуст, возвращает None
    """
    # Ваш код здесь
    if numbers:
        return max(numbers)
    return None


def filter_even_numbers(numbers):
    """
    Возвращает новый список, содержащий только четные числа из списка numbers
    """
    # Ваш код здесь
    return [i for i in numbers if i % 2 == 0]


def generate_multiplication_table(n):
    """
    Возвращает таблицу умножения размером n x n в виде списка списков
    Например, для n=3 результат должен быть:
    [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    """
    # Ваш код здесь
    return [
        [i for i in range(j, (n+1)*j, j)]
        for j in range(1, n+1)
    ]
