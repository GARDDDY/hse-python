# Задание 4: Условные операторы (if-else)
# Реализуйте функции с использованием условных операторов


def is_positive(number):
    """
    Возвращает True, если число положительное, иначе False
    """
    # Ваш код здесь
    return True if number > 0 else False


def is_even(number):
    """
    Возвращает True, если число четное, иначе False
    """
    # Ваш код здесь
    return False if number % 2 else True


def is_in_range(number, start, end):
    """
    Возвращает True, если число находится в диапазоне [start, end], иначе False
    """
    # Ваш код здесь
    return number in range(start, end+1)


def max_of_three(a, b, c):
    """
    Возвращает максимальное из трех чисел
    """
    # Ваш код здесь
    return max([a, b, c])


def fizz_buzz(number):
    """
    Если число делится на 3, возвращает "Fizz"
    Если число делится на 5, возвращает "Buzz"
    Если число делится и на 3, и на 5, возвращает "FizzBuzz"
    Иначе возвращает само число в виде строки
    """
    # Ваш код здесь
    fizzbuzz_string = ("Fizz" if number % 3 == 0 else "") \
        + ("Buzz" if number % 5 == 0 else "")
    return str(number) if len(fizzbuzz_string) == 0 else fizzbuzz_string


def grade_converter(score):
    """
    Конвертирует числовую оценку в буквенную:
    90-100: 'A'
    80-89: 'B'
    70-79: 'C'
    60-69: 'D'
    0-59: 'F'
    Если score не в диапазоне 0-100, возвращает 'Invalid score'
    """
    # Ваш код здесь
    if score not in range(0, 100+1):
        return "Invalid score"
    return {10: "A", 9: "A", 8: "B", 7: "C", 6: "D"}.get(score//10, "F")
