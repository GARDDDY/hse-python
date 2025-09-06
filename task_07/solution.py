# Задание 7: Списки и операции со списками
# Реализуйте функции для работы со списками


def create_list(start, end, step=1):
    """
    Создает список чисел от start до end (включительно) с шагом step
    """
    # Ваш код здесь
    return list(range(start, end+1*(abs(step)//step), step))


def find_element_index(lst: list, element):
    """
    Находит индекс первого вхождения элемента в список
    Если элемент не найден, возвращает -1
    """
    # Ваш код здесь
    try:
        return lst.index(element)
    except ValueError:
        return -1


def remove_duplicates(lst):
    """
    Удаляет дубликаты из списка, сохраняя порядок элементов
    """
    # Ваш код здесь
    return list(set(lst))


def merge_lists(list1, list2):
    """
    Объединяет два списка в один, удаляя дубликаты
    """
    # Ваш код здесь
    return list(set(list1) | set(list2))


def list_intersection(list1: list, list2: list):
    """
    Возвращает список элементов, которые есть в обоих списках
    """
    # Ваш код здесь
    return list(set(list1).intersection(set(list2)))


def list_difference(list1, list2):
    """
    Возвращает список элементов, которые есть в list1, но отсутствуют в list2
    """
    # Ваш код здесь
    return list(set(list1) - set(list2))


def flatten_list(nested_list):
    """
    Преобразует вложенный список в плоский
    Например, [1, [2, 3], [4, [5, 6]]] -> [1, 2, 3, 4, 5, 6]
    """
    # Ваш код здесь
    def flatten(nested_list):
        for i in nested_list:
            if isinstance(i, list):
                yield from flatten_list(i)
            else:
                yield i
    return list(flatten(nested_list))
