# Задание 9: Словари
# Реализуйте функции для работы со словарями


def create_person(name, age, city):
    """
    Создает и возвращает словарь, представляющий человека
    с ключами 'name', 'age', 'city'
    """
    # Ваш код здесь
    return {
        "name": name,
        "age": age,
        "city": city
    }


def get_value(dictionary: dict, key, default=None):
    """
    Возвращает значение из словаря по ключу
    Если ключ отсутствует, возвращает default
    """
    # Ваш код здесь
    return dictionary.get(key, default)


def update_dict(dictionary, key, value):
    """
    Обновляет словарь, добавляя или изменяя пару ключ-значение
    Возвращает обновленный словарь
    """
    # Ваш код здесь
    dictionary[key] = value
    return dictionary


def merge_dicts(dict1, dict2):
    """
    Объединяет два словаря в один новый
    Если ключи повторяются, значения из dict2 имеют приоритет
    """
    # Ваш код здесь
    pass


def invert_dict(dictionary: dict):
    """
    Создает новый словарь, где ключи и значения поменяны местами
    Предполагается, что значения в исходном словаре уникальны
    """
    # Ваш код здесь
    new_dict = {}
    for k, v in dictionary.items():
        new_dict[v] = k

    return new_dict


def count_words(text):
    """
    Подсчитывает количество вхождений каждого слова в тексте
    Возвращает словарь, где ключи - слова, значения - количество вхождений
    Слова приводятся к нижнему регистру и очищаются от знаков препинания
    """
    # Ваш код здесь
    import string
    import re
    import collections
    text = re.sub(string.punctuation, "", text)
    return collections.Counter(text.split())


def filter_by_value(dictionary, condition):
    """
    Фильтрует словарь по значению, используя функцию condition
    Возвращает новый словарь с парами, для которых condition(value) == True

    Пример использования:
    filter_by_value({'a': 1, 'b': 2, 'c': 3}, lambda x: x > 1)
    Вернет: {'b': 2, 'c': 3}
    """
    # Ваш код здесь
    pass
