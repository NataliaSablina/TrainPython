from functools import reduce

a = [1, 2, 3, 4]
a.reverse()  # исходный список меняется
print(a)
a.reverse()
print(a)
print(a[::-1])  # исходный список не меняется


def change(lst):
    a = lst[0]
    b = lst[-1]
    lst[0] = b
    lst[-1] = a
    return lst


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# def change(lst):
#     new_start = lst.pop()  # Удаляем последний элемент и сохраняем его в переменную
#     new_end = lst.pop(0)  # Удаляем первый элемент и сохраняем его в переменную
#     lst.append(new_end)  # Добавляем к списку новый последний элемент
#     lst.insert(0, new_start)  # Добавляем к списку новый первый элемент
#     return lst


print(change([1, 2, 3, 4]))


def to_list(*args):
    lst = list(args)
    return lst


print(to_list(1, 2, 3, 3, 34, 4, 4, 9))


# def useless(s):
#     el = max(s, key = lambda i: int(i))
#     le = len(s)
#     return el//le

def useless(lst):
    return max(lst) / len(lst)


print(useless([8, 9, 12]))


def list_sort(lst):
    lst.sort(reverse=True)
    return lst


print(list_sort([9, 4, -1, 4]))


def all_eq(lst):

    max_str = max(lst, key=len)
    lst2=[]
    for lst_string in lst:
        if len(lst_string) < len(max_str):
            while len(lst_string) < len(max_str):
                lst_string += '_'
        lst2.append(lst_string)
    return lst2
# def all_eq(lst):
# max_item = max(lst, key=lambda x: len(x))
# max_len = len(max_item)
# return [item.ljust(max_len, '_') for item in lst]


print(all_eq(['rt', 'jigrhifjkkoidugynv', 'i', 'kfojkg']))


def del_even(lst):
    new_lst = [i for i in lst if i % 2 != 0]
    return new_lst


print(del_even([2, 5, 7, 6, 8]))

lst1 = [5, 1, 6, 34, 2]
lst2 = [0, 8, 2, 6, 3]

lst1.sort()
lst2.sort()
lst1.extend(lst2)
print(lst1)

minimum = min(lst1, key=lambda i: int(i))
print(minimum)

lts3 = [[2, 4, 5], [10, 98, 56], [9, 0, 1]]
res = reduce(lambda i, j: i if sum(i) > sum(j)

                            else j, lts3)
print(res)


def alphabet_position(text):
    alphabet_list =list("abcdefghijklmnopqrstuvwxyz")
    print(alphabet_list)
    text2 = text.lower()
    number =""
    for letter in text2:
        for el in alphabet_list:
            if letter == el:
                number += str(alphabet_list.index(el)+1)+" "

    return number


print(alphabet_position("Cat and dog"))

