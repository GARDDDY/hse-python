# Задание 3: Строки и операции со строками
# Реализуйте функции для работы со строками


def string_length(s: str):
    """
    Возвращает длину строки
    """
    # Ваш код здесь
    return len(s)


def string_concatenation(s1: str, s2: str):
    """
    Соединяет две строки
    """
    # Ваш код здесь
    return s1+s2


def string_to_uppercase(s: str):
    """
    Преобразует строку к верхнему регистру
    """
    # Ваш код здесь
    return s.upper()


def string_to_lowercase(s: str):
    """
    Преобразует строку к нижнему регистру
    """
    # Ваш код здесь
    return s.lower()


def string_replace(s: str, old: str, new: str):
    """
    Заменяет в строке s все вхождения подстроки old на new
    """
    # Ваш код здесь
    return s.replace(old, new)


def string_split(s: str, delimiter):
    """
    Разбивает строку по указанному разделителю
    """
    # Ваш код здесь
    return s.split(delimiter) if delimiter != "" else list(s)


def string_strip(s: str):
    """
    Удаляет начальные и конечные пробелы из строки
    """
    # Ваш код здесь
    return s.strip()


def is_palindrome(s: str):
    """
    Проверяет, является ли строка палиндромом
    (читается одинаково слева направо и справа налево)
    Регистр и пробелы не учитываются
    """
    # Ваш код здесь
    s = s.replace(" ", "").lower()
    return s == s[::-1]
