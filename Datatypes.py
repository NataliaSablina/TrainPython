from functools import reduce
from sys import getsizeof

lst = [1, 2, 3, 3, 3, 4, 5]
lst.append("Cat")
print(lst)
lst[4] = 9
print(lst)
lst.insert(4, 9)
print(lst)
lst.append([2, 5, 6])
print(lst)
lst[-3] = (3, 4, 6)
print(lst)
print(lst[0])
lst.remove(1)
print(lst)
print(lst.count(3))
print(lst[0])
print(lst[-1])

a = 2
b = 3
print(a, b)
a, b = b, a
print(a, b)

lst = [1, 2, 3, 3, 3, 4, 5]
slt = set(lst)
print(len(slt) == len(lst))

dct = {1: "Cat", 2: "Dog"}
dct[3] = "Frog"
print(dct[3])

dct[(2, 3, 4)] = [9, 0, 8]
print(dct.get((2, 3, 4)))
dct.pop(2)

keys = dct.keys()
print(keys)

f1 = {1, 2, 3}
print(f1)
# s5 = {1, 2, 3, [5, 6, 7, 8]}
# print(s5)

f3 = {7, 8, 9}
f2 = frozenset(f1)
print(f2)

f5 = {2, 6, 7}
f4 = f1 | f3
print(f4)

f6 = f1 & f5
print(f6)

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x for x in list_a if x % 2 == 0]
print(list_b)

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x ** 2 for x in list_a]
print(list_b)

list_a = ['a', 'abc', 'abcde']
list_b = [len(x) for x in list_a]
print(list_b)

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x if x < 0 else x ** 2 for x in list_a]
# Если x-отрицательное - берем x, в остальных случаях - берем квадрат x
print(list_b)  # [-2, -1, 0, 1, 4, 9, 16, 25]

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x ** 3 if x < 0 else x ** 2 for x in list_a if x % 2 == 0]
# вначале фильтр пропускает в выражение только четные значения
# после этого ветвление в выражении для отрицательных возводит в куб, а для остальных в квадрат
print(list_b)  # [-8, 0, 4, 16]

numbers = range(10)

# Before
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]

# After
squared_evens = [
    n ** 2
    for n in numbers
    if n % 2 == 0
]

lst1 = [8, 9, 3, 5, 6]
lst1.reverse()
print(lst1)
print(lst1[::-1])


def change(lst):
    if len(lst) < 2:
        return "В списке должно быть больше 2ух элементов"

    # a = lst[0]
    # b = lst[-1]
    # lst[0] = b
    # lst[-1] = a

    # new_start = lst.pop()  # Удаляем последний элемент и сохраняем его в переменную
    # new_end = lst.pop(0)  # Удаляем первый элемент и сохраняем его в переменную
    # lst.append(new_end)  # Добавляем к списку новый последний элемент
    # lst.insert(0, new_start)  # Добавляем к списку новый первый элемент

    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


lst = [2, 3, 4]
print(change(lst))


def to_list(*args):
    return list(args)


print(to_list(1, 2, 3, 4))


def useless(lst):
    return max(lst) / len(lst)


lst = [6, 7, 789, 34, 67, 1234]
print(useless(lst))


def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst


lst = [9, 1, 2, 3, 10, 4]
print(list_sort(lst))


def ed_aq(lst):
    max_string = max(lst, key=len)
    print(max_string)
    lst2 = []
    for x in lst:
        if len(x) < len(max_string):
            while len(x) < len(max_string):
                x = x + "_"

            print(x)
        lst2.append(x)

    return lst2


lst = ["Fuck", "Fact", "a", "unique"]
print(ed_aq(lst))


class C:
    def abc(self):
        return ('иди')


class A:
    x = 2

    def generate_new_class(self, class_name):
        return type(class_name, (C,), {"x": self.x})

    def __str__(self):
        return 'экземпляр'


print(A)
print(A())
print(A().generate_new_class('C')().abc())

# def descending_order(num):
#     num2=list(num)
#     num2.reverse()
#     num3=int(num2)
#     return num3
#
#
#
# num=987
# print(descending_order(num))

dict_1 = dict(key1='value1', key2=4)
print(dict_1)
dict_1.update({"1": 1, "2": 2})
print(dict_1)
dict_1.update({(1, 2, 3): [1, 2, 3]})
print(dict_1)
print(dict_1['key1'])
print(dict_1.pop('key3', 3))
print(dict_1.keys())

st1 = set({1, 2, 3})
st2 = frozenset({2, 5, 6})
print(st2)
print(st1.intersection(st2))
print(st1.union(st2))


def to_dict(lst):
    lst_dict = dict()
    for i in lst:
        lst_dict.update({i: i})
    return lst_dict


# def to_dict(lst):
#     return {element: element for element in lst}


lst = [1, 2, 3]
print(to_dict(lst))


def biggest_dict(**kwargs):
    big_dict = {"first one": "we can do it"}
    for key, value in kwargs.items():
        big_dict.update({key: value})
    return big_dict


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


print(biggest_dict(dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon"))


def count_it(sequence):
    digits_number = dict()
    for i in sequence:
        digits_number.update({i: sequence.count(i)})
    sorted_rooms = sorted(digits_number.items(), key=lambda item: item[1])
    sorted_rooms_2 = dict(sorted_rooms[-3:])
    sorted_rooms_3 = dict(sorted(sorted_rooms_2.items(), key=lambda item: item[1], reverse=True))
    return sorted_rooms_3


digits_str = "1233345628172364524781"
print(digits_str.count('1'))
print(count_it(digits_str))

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
# Результат выполнения
# {1: 10, 2: 3}
# {3: 8, 1: 7, 5: 7}
# {7: 6, 4: 6, 6: 3}


constant_dict = {'cat': 'Maggie', 'dog': 'Lucky', 'frog': "Spot", 'fox': 'Devid', 'wolf': 'Grey'}
print(id(constant_dict))
print(constant_dict)
constant_dict.pop('dog')
print(id(constant_dict))
print(constant_dict)
constant_dict.update({'new_key': 'new_dict'})
print(id(constant_dict))
print(constant_dict)

from collections import OrderedDict

ordered_constant_dict = OrderedDict({'cat': 'Maggie', 'dog': 'Lucky', 'frog': "Spot", 'fox': 'Devid', 'wolf': 'Grey'})
print(id(ordered_constant_dict))
print(ordered_constant_dict)
first = list(ordered_constant_dict.items())[0]
last = list(ordered_constant_dict.items())[-1]

ordered_constant_dict.move_to_end(key=first[0])
ordered_constant_dict.move_to_end(key=last[0], last=False)
print(id(ordered_constant_dict))
print(ordered_constant_dict)

second = list(ordered_constant_dict.items())[1]
ordered_constant_dict.pop(key=second[0])
print(id(ordered_constant_dict))
print(ordered_constant_dict)

ordered_constant_dict.update({'new_key': 'new_dict'})
print(id(ordered_constant_dict))
print(ordered_constant_dict)

from collections import Counter


def max_dict(*dicts):
    pass


def sum_dict(*dicts):
    summa = Counter()
    for dictionary in dicts:
        summa.subtract(dictionary)
    return summa


def test_func(a, b):
    print(a, ' - ', b)
    return Counter(a) + Counter(b)


def sum_dct(*dicts):
    return dict(reduce(test_func, dicts))


def max_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))


dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

print(max_dct(dict_1, dict_2))
print(sum_dct(dict_1, dict_4, dict_3))
print(dict_1.values())

# print({1: 2, 3: 3} + {'a': 0, 'b': 0})

d = {'a': 0, 'b': 0}
for i in d:
    print(i)

#
# d2 = {(1,2, [3, 4]):"cat"}
# print(d2)

storm_1 = 'Lightning'
Union = (' and ')
storm_2 = ('Thunder')

print(storm_1 + Union + storm_2)


def sort_tpl(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))


tpl = (3, 1, 5.5, 7)
print(sort_tpl(tpl))


def slicer(tpl, element):
    if tpl.count(element) > 1:
        first = tpl.index(element)
        last = tpl.index(first + 1, element)
        print('last', last)
        return tuple(tpl[first:last + 1])
    if tpl.count(element) == 1:
        first = tpl.index(element)
        return tuple(tpl[first + 1::])
    if tpl.count(element) == 0:
        return tuple([])


print(slicer((1, 2, 3, 2, 5), 6))


def seive(tpl):
    return tuple(reversed(list(set(tpl))))


print(seive([11, 3, 5, 1, 1]))


#
# def sieve(lst):
#     unique = []
#     [unique.append(item) for item in reversed(lst) if item not in unique]
#     return tuple(unique)


def delete_from_tuple(tpl, el):
    if el in tpl:
        elem = tpl.index(el)
        return tpl[:elem] + tpl[elem + 1:]
    return tpl


print(delete_from_tuple((1, 2, 3, 4, 5), 4))

from collections import namedtuple

student = namedtuple('Student', "name age mark town")
students = (
    student(name="Alex", age=18, mark=9.5, town="Madrid"),
    student(name="Kristina", age=19, mark=7.0, town="Madrid"),
    student(name="Gleb", age=19, mark=9.98, town="Katowice"),
    student(name="Natalia", age=18, mark=9.97, town="Katowice"),
    student(name="Anastasia", age=19, mark=9.6, town="Minsk"),
    student(name="Marina", age=19, mark=6.57, town="Minsk"),
    student(name="Alina", age=18, mark=9.0, town="Minsk"),
)


def good_students(students):
    sum_mark = 0
    for student in students:
        sum_mark += student.mark
    middle_mark = sum_mark / len(students)
    good_students_list = []
    for student in students:
        if student.mark >= middle_mark:
            good_students_list.append(student.name)
    tuple(good_students_list)

    good_students_str = ", ".join(good_students_list)
    return "Ученики " + good_students_str + " в этом семестре хорошо учатся!"


print(good_students(students))


def to_set(data):
    data_set = set(data)
    len_data = len(data_set)
    return data_set, len_data


print(to_set('frtsdddddreh'))


def list_to_set(lst):
    lst_2 = []
    for i in lst:
        try:
            hash(i)
            lst_2.append(i)
        except TypeError:
            print("TypeError")
    return set(lst_2)


lst = [1, 2, 3, [1, 2, 3], 4, 6, ["kfjvf"]]
print(list_to_set(lst))

from collections.abc import Hashable


def list_to_set_2(lst):
    st = {item for item in lst if isinstance(item, Hashable)}
    print(st)


list_to_set_2(lst)


def diff(set_1, set_2, set_3, symmetric=True):
    if symmetric:
        return set_1 ^ set_2 ^ set_3
    return set_1 - set_2 - set_3


set_1 = {3, 4, 5, 6, 20}
set_2 = {4, 6, 7, 8, 9}
set_3 = {5, 3, 8, 1}
print(diff(set_1, set_2, set_3))
print(diff(set_1, set_2, set_3, False))


def superset(set_1, set_2):
    if set_1 > set_2:
        return f"{set_1} является чистым супермножеством"
    if set_1 < set_2:
        return f"{set_2} является чистым супермножеством"
    if set_1 == set_2:
        return f"множества равны"
    if not (set_1.issuperset(set_2) or set_2.issuperset(set_1)):
        return f"супермножества не обнаружены"


set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}

print(superset(set_1, set_2))
print(superset(set_1, set_3))
print(superset(set_2, set_3))
print(superset(set_4, set_2))


def set_gen(lst):
    index = 0
    while index < len(lst):
        cnt = lst.count(lst[index])
        if cnt > 1:
            lst[index] = str(lst[index]) * cnt
        index += 1

    return set(lst)


lst_3 = [1, 2, 3, 4, 4, 5, 5, 2, 4]
print(set_gen(lst_3))

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))


st_1 = {3, 7, 8, 89}
st_2 = {7, 89}

print(11*2**2-13/4+7)

# print(round(getsizeof(3**9090001)/(1024*1024), 2))

print(4**4**4)

# print(int('123e'))
# print(int('91.4'))
# print(int(524.345 ** 435345345311145345))
# print(int('7.1 + 4'))
# print(int('4'-2))
# print(int('4-2'))
print(int('42'))
print(int(-12.12))


def pos_add(a, b):
    return abs(a + b)


print(pos_add(-1, -2))


def foo4(a):
    return divmod(a, -11)


print(foo4(22))


def sun_num(number):
    if isinstance(number, int) and not isinstance(number, bool):
        print(88)
        return sum(map(int, list(str(abs(number)))))
    else:
        return f'Это не целое число'


print(sun_num(123))


def magic(number_str, magic_number):
    list_number = map(int, list(number_str))
    square_sum = sum([i*i for i in list_number])
    if square_sum % magic_number == 0:
        return f'Магия случилась'
    else:
        return f'Нет магии'


print(magic('123', 3))

# def magic(*args, k):
#    # 1. Начальная сумма равна нулю
#    sq_sum = 0
#    # 2. Складываем квадраты всех аргументов в цикле
#    for i in args:
#        sq_sum += i ** 2
#    # 3. Определяем, равен ли остаток от деления sq_sum на k нулю
#    if sq_sum % k == 0:
#        return 'Волшебство случается'
#    return 'Никакого волшебства'
#
# # Тесты
# print(magic(2, 5, 7, k=5))
# print(magic(2, 5, 7, k=39))
# print(magic(2, 5, 7, k=2))


def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return "Невозможно преобразовать"


print(to_float(12))
print(to_float(-1.762))
print(to_float(True))
print(to_float('Не число'))
print(to_float('2.2'))


def avg_5(a, b, c, d):
    return round((a + b + c + d) / 4, 5)

# Тесты
print(avg_5(1, 6, 7, 4))
print(avg_5(1.7, 6.2, 2, 6))
print(avg_5(3, -3.143223442, -4.76, 1.3902))


def mul_to_int(a, b):
    res = a * b
    if float(res).is_integer():
        return int(res)
    return res

# Тесты
print(mul_to_int(2, 4))
print(mul_to_int(2.5, 4))
print(mul_to_int(2.2, 2))


from math import pi


print((3 * 36 / (4 * pi)) ** (1/3))


def round_standard(num):
    if num >= 0:
        sign = 1
    else:
        sign = -1
    return sign * int((abs(num) + 0.5))


# Тесты
print(round_standard(1.5))
print(round_standard(-2.5))
print(round_standard(1.6))
print(round_standard(5.11))


def eqv(a, b, c):
    res = a+ b
    e = 0.01/100
    tolerance= e*max(abs(a), abs(b))
    return abs(res-c) <= tolerance


print(eqv(0.12, 0.31, 0.43))
print(eqv(0.1, 0.2, 0.3))
print(eqv(0.1, 0.2, 0.4))
print(eqv(-0.1, -0.2, -0.3))


def eqv(a, b, c):
    from math import isclose
    return isclose(a + b, c, rel_tol=0.01 / 100, abs_tol=0)

# Тесты
print(eqv(0.12, 0.31, 0.43))
print(eqv(0.1, 0.2, 0.3))
print(eqv(0.1, 0.2, 0.4))
print(eqv(-0.1, -0.2, -0.3))


def search_substring(substring, str):
    if substring.lower() in str.lower():
        return 'Есть контакт!'
    else:
        return 'Мимо!'


# Тесты
print(search_substring('Кол', 'коЛокОл'))
print(search_substring('Колобок', 'колобоК'))
print(search_substring('Кол', 'Плов'))

print(search_substring('o', 'ku'))


def find_index(letter, st):
    if letter in st:
        return st.index(letter), st.rindex(letter)
    else:
        return None, None


print(find_index('o', 'oo'))


# from collections import Counter
#
# word = 'приоритет'
# c = Counter(word)
# print(c.most_common(3))

from collections import Counter


def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])


# Тесты
print(top3('Улыбкой ясною природа Сквозь сон встречает утро года Синея блещут небеса. Еще прозрачные, леса'))
print(top3('АаА'))
print(top3('Голова думала'))


def camel(st):
    new_st = ''
    letter_counter = 0
    for  val in st:
        if val.isalpha():
            if letter_counter % 2 == 0:
                new_st += val.upper()
            else:
                new_st += val.lower()
            letter_counter += 1
        else:
            new_st += val
    return new_st


# Тесты
print(camel('Утром!! было! солнечно!!!!'))
print(camel('КРАСОТА)))'))
print(camel('дождливЫЙ, вечеР??'))


def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
        print(st)
    return st


# Тесты
print(shortener('Падал(лишнее (лишнее) лишнее) прошлогодний снег (лишнее)'))
print(shortener('(лишнее(лишнее))Падал прошлогодний (лишнее(лишнее(лишнее)))снег'))


def cleaned_str(st):
    clean_lst = []
    for symbol in st:
        if symbol == '@' and clean_lst:
            clean_lst.pop()
        elif symbol != '@':
            clean_lst.append(symbol)
    return ''.join(clean_lst)


# Тесты

print(cleaned_str('гр@оо@лк@оц@ва'))
print(cleaned_str('сварка@@@@@лоб@ну@'))

dog_do = ['woof!']
dog_do_2 = ['woof!']
print(dog_do + dog_do_2)

tuple_11 = (1, 2, 3, [1, 2, 3])
print(id(tuple_11), tuple_11)
tuple_11[3][2] = 1
print(id(tuple_11), tuple_11)

# set_11 =  {1, 2, [1, 2]}
# str_111="henfj"
# str_111[1]='i'

import math
print(math.__doc__)
print(ord('a'))
print(chr(345))
print(ord('€'))
print(ord('∑'))

s = 'python'
print(id(s))
s = s.replace('h', 't')
print(id(s))


