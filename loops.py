import gc
import numpy as np
import random


def more_than_five(lst):
    more_5 = []
    for i in lst:
        if abs(i) > 5:
            more_5.append(i)
    return more_5


print(more_than_five([-11, 4, -2, 90, 400, 0, -5]))
print(more_than_five([-2, 2, 3, 4, 0, -1]))
print(more_than_five([70, -900, 41, 0]))

letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
new_string = ''
string_lst = []

for letter in letters:
    if letter != letter.upper():
        string_lst.append(letter)

new_string = ''.join(string_lst)
print(new_string)

# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# clean_string = ''
# for letter in letters:
#     if not letter.isupper():
#         clean_string += letter
# letters = clean_string
# print(letters)


rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for position in range(11):
    print('^' * 27)
    for letter in rus_lower:
        if rus_lower.index(letter) % 11 == position:
            print('| ', letter.upper(), letter, ' |', end='')
    print()
print('^' * 27)


#
# lst_secret = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]
# p = input()
# while p not in lst_secret:
#     print("Тут ничего нет. Еще есть вопросы?")
#     p = input()
# else:
#     print(f"Ты – свой. Приветствую, любезный {p}!")


# def all_divisors(number):
#     number_lst = []
#     div_number = 1
#     while div_number <= number/2:
#         if number % div_number == 0:
#             number_lst.append(div_number)
#         div_number += 1
#     number_lst.append(number)
#     return number_lst
#
#
# print(all_divisors(6))

def all_divisors(number):
    lst = [1, number]
    for i in range(2, 1 + int(number ** 0.5)):
        if number % i == 0:
            lst.extend({number // i, i})
    return sorted(lst)

# Тесты
# print(all_divisors(23_436))
# print(all_divisors(190_187_200))
# print(all_divisors(380_457_890_232))


a = 2
b = a
b = 9
print(a)

print(gc.get_stats())
print(gc.garbage)

lst_111 = [1, 2, 3]
lst_222 = [1, 2, 3]
print(id(lst_111), id(lst_222))

a1 = 1
b1 = 1
print(id(a1), id(b1))

tuple_1 = ([1, 2], 2)
print(id(tuple_1))
tuple_1[0].append(3)
print(id(tuple_1), tuple_1)


a = None

num_lst = []
for i in range(5):
    num_lst.append(random.randrange(-20, 20, 3))

print(num_lst)

num_ls_2 = list(range(0, 100, 17))
print(num_ls_2)

lst_digit = [1, -1, 6, 7, -2]


def calc_digit(lst):
    i = 0
    for el in lst:
        if el < 0:
            i += 1
    return lst, i


print(calc_digit(lst_digit))


def letter_count(lst):
    letters_count = []
    for word in lst:
        letters_count.append(len(word))
    return lst, letters_count


words_lst = ['yes', 'no', 'maybe', 'ok', 'what']
print(letter_count(words_lst))


eng = ['yes', 'no', 'maybe', 'ok', 'what']
rus = ["да", "нет", "наверно", "ок", "что"]


def button_change(str):
    if str in eng:
        index = eng.index(str)
        return rus[index]


print(button_change('yes'))



