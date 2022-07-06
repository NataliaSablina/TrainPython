from collections import OrderedDict


def pack(**kwargs):
    print(kwargs)

    def inner_pack():
        nonlocal kwargs
        arg1, arg2 = kwargs.items()
        kwargs.update(dict(key3=4, key4=6))
        print(kwargs)
        print(arg1, arg2)

    inner_pack()


pack(key1=2, key2=3)


def pack2(*args):
    print(args)
    arg1, arg2 = args
    print(arg1, arg2)
    args = 8, 9
    print(args)


pack2(3, 4)


def to_dict(lst: list) -> dict:
    new_dict = {x: x for x in lst}
    return new_dict


print(to_dict([1, 2, 3]))


def biggest_dict(biggest={}, **kwargs):
    biggest.update(kwargs)
    print(biggest)


biggest_dict(key1=1, key2=2)
biggest_dict(key3=3, key4=4)


# my_dict = {'first_one': 'we can do it'}
#
#
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
#
#
# biggest_dict(k1=22, k2=31, k3=11, k4=91)
# biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
# print(my_dict)


def count_it(sequence: str) -> dict:
    sequence_dict = {int(x): sequence.count(x) for x in sequence}
    sorted_dict = dict(sorted(sequence_dict.items(), key=lambda item: item[1])[-1:-4:-1])
    return sorted_dict


print(count_it('839247777834499'))


# from collections import Counter
#
#
# def count_it(sequence):
#     return dict(Counter([int(num) for num in sequence]).most_common(3))
#
# # Тесты
# print(count_it('1111111111222'))
# print(count_it('123456789012133288776655353535353441111'))
# print(count_it('007767757744331166554444'))


ordered_dict = OrderedDict(key1=1, key2=2, key3=3, key4=4, key5=5)
print(id(ordered_dict))
ordered_dict.move_to_end('key1')
ordered_dict.move_to_end('key5', last=False)
print(id(ordered_dict))
ordered_dict.update({'new_key':'new_value'})
print(ordered_dict)





# Задача 5. * Продвинутый уровень
# Условие
#
# Имеется ряд словарей с пересекающимися ключами (значения - положительные числа). Напишите 2 функции, которые делают с массивом словарей следующие операции:
# 1-ая функция max_dct(*dicts) формирует новый словарь по правилу:
#
# Если в исходных словарях есть повторяющиеся ключи, выбираем среди их значений максимальное и присваиваем этому ключу (например, в словаре_1 есть ключ “а” со значением 5, и в словаре_2 есть ключ “а”, но со значением 9. Выбираем максимальное значение, т. е. 9, и присваиваем ключу “а” в уже новом словаре).
#
# Если ключ не повторяется, то он просто переносится со своим значением в новый словарь (например, ключ “с” встретился только у одного словаря, а у других его нет. Следовательно, переносим в новый словарь этот ключ вместе с его значением). Сформированный словарь возвращаем.
#
# 2-ая функция sum_dct(*dicts) суммирует значения повторяющихся ключей. Значения остальных ключей остаются исходными. (Проводятся операции по аналогу первой функции, но берутся не максимумы, а суммы значений одноименных ключей). Функция возвращает сформированный словарь.
# Для проверки работоспособности создадим 4 словаря. Чтобы максимально упростить решение и сделать его «питоничным», воспользуемся модулем collections и его классом Counter, а также функцией reduce из модуля functools.
# Решение — IDE
#
# from collections import Counter
# from functools import reduce
# dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
# dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
# dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
# dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}
#
#
# def sum_dct(*dicts):
#     return dict(reduce(lambda a, b: Counter(a) + Counter(b), dicts))
#
# def max_dct(*dicts):
#     return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))
#
# # Тесты
# print(max_dct(dict_1, dict_2))
# print(sum_dct(dict_1, dict_4, dict_3))
# print(max_dct(dict_1, dict_2, dict_3, dict_4))
# print(sum_dct(dict_1, dict_2, dict_3, dict_4))
# Результат выполнения
#
# {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90, 7: 112}
# {1: 12, 2: 36, 3: 14, 4: 83, 5: 33, 6: 98, 9: 9, 10: 556, 7: 25, 8: 71}
# {1: 12, 2: 33, 3: 10, 4: 60, 5: 31, 6: 90, 7: 112, 8: 71, 9: 9, 10: 556}
# {1: 24, 2: 36, 3: 21, 4: 84, 5: 35, 6: 98, 7: 137, 8: 71, 9: 9, 10: 556}
# Так как функции отличаются только операцией, а весь код повторяется, их можно упростить за счет модуля operator и дополнительной функции-обработчика dict_transformer().
# Решение — IDE
#
# from collections import Counter
# from functools import reduce
# from operator import or_, add
#
# def sum_dct(*dicts):
#     return dict_transformer(*dicts)
#
# def max_dct(*dicts):
#     return dict_transformer(*dicts, op=or_)
#
# def dict_transformer(*dicts, op=add):
#     return dict(reduce(lambda a, b: op(Counter(a), Counter(b)), dicts))
#
#
# # Тесты
# print(max_dct(dict_1, dict_2))  # Ищем максимум
# print(sum_dct(dict_1, dict_4, dict_3))  # Складываем
# print(max_dct(dict_1, dict_2, dict_3, dict_4))  # Ищем максимум
# print(sum_dct(dict_1, dict_2, dict_3, dict_4))  # Складываем
# Результат выполнения
#
# {1: 12, 2: 33, 3: 10, 4: 60, 5: 2, 6: 90, 7: 25, 8: 71}
# {1: 12, 2: 36, 3: 14, 4: 83, 5: 33, 6: 98, 9: 9, 10: 556, 7: 25, 8: 71}
# {1: 12, 2: 33, 3: 10, 4: 60, 5: 31, 6: 90, 7: 112, 8: 71, 9: 9, 10: 556}
# {1: 24, 2: 36, 3: 21, 4: 84, 5: 35, 6: 98, 7: 137, 8: 71, 9: 9, 10: 556}
