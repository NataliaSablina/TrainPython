def zero(operation=None):  # your code here
    return 0 if operation == None else operation(0)


def one(operation=None):  # your code here
    return 1 if operation == None else operation(1)


def two(operation=None):  # your code here
    return 2 if operation == None else operation(2)


def three(operation=None):  # your code here
    return 3 if operation == None else operation(3)


def four(operation=None):  # your code here
    return 4 if operation == None else operation(4)


def five(operation=None):  # your code here
    return 5 if operation == None else operation(5)


def six(operation=None):  # your code here
    return 6 if operation == None else operation(6)


def seven(operation=None):  # your code here
    return 7 if operation == None else operation(7)


def eight(operation=None):  # your code here
    return 8 if operation == None else operation(8)


def nine(operation=None):  # your code here
    return 9 if operation == None else operation(9)


def plus(x):  # your code here
    return lambda y: y + x


def minus(x):  # your code here
    return lambda y: y - x


def times(x):  # your code here
    return lambda y: y * x


def divided_by(x):  # your code here
    return lambda y: y // x


def f(a=1, b=2, c=3):
    return a + b + c


params = {'a': 10, 'b': 20}
S = f(**params)
print(S)


# def inplace(x, mutable=[]):
#    mutable.append(x)
#    return mutable

def inplace(x, lst=None):
    if lst is None: lst = []
    lst.append(x)
    return lst


res = inplace(1)
res = inplace(2)
print(inplace(3))


#
# print(inplace.__call__)
# print(inplace.__class__)
# print(inplace.__sizeof__)
# print(inplace.__closure__  )
# print(inplace.__hash__ )
# print(inplace.__reduce__ )
# print(inplace.__str__)
# print(inplace.__code__)
# print(inplace.__format__)
# print(inplace.__init__)
# print(inplace.__reduce_ex__)
# print(inplace.__subclasshook__)
# print(inplace.__defaults__)
# print(inplace.__get__)
# print(inplace.__repr__)
# print(inplace.__delattr__)
# print(inplace.__getattribute__)
# print(inplace.__setattr__)
# print(inplace.__class__)
# print(inplace.__dict__)
# print(inplace.__globals__)
# print(inplace.__new__)
#
#
# import time
#
# numbers = range(100, 100_000_000)
# start = time.perf_counter()
# for number in numbers:
#     pass
# print(time.perf_counter() - start)


def eee(x):
    if x < 2:
        pass
    else:
        print(9)


eee(4)


def my_func(a, b):
    print(a, b)


my_func(2, 4)
my_func(b=2, a=4)

for i in range(0, 100):
    pass
else:
    print("888888")


def factorial(n):
    try:
        assert n > 0
    except:
        print('uuuuuuuu')
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(4))

i = 0


def increment():
    global i
    i += 1


def func(x): return x


a1 = func
print(a1(10))

func = lambda x, y: x + y
print(func(1, 2))

l = (lambda e: e - 2)
print(l(-1))

c, b = 1, 2


# y=lambda c,b:c+b
# y()

#
# y=lambda c:c+b
# y()
#
#
# y = lambda: c + b
# print(y())
#
#
# def abc():
#     a = b + c
#     return a


def prod(a: int, b: int) -> int:
    return a / b


def outerFunc():
    def firstInner():
        print('This is first inner function')

    def secondInner():
        print('This is second inner function')

    firstInner()
    secondInner()


outerFunc()

print(help(outerFunc))

print(max(1, 2, 3, 4))
print(min(1, 2, 3, 4))
print(list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4])))

from functools import reduce

num = [4, 2, 3, 4]
print(reduce(lambda x, y: x ** y, num))

print(tuple(zip([1, 2, 3], [89, 90, 91])))
print(ascii(max))

# x = compile("x = 1\n z = 2\n print(x+z)", 'functions', 'eval')
# print(eval(x))


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(globals() == locals())
print(hash((3, 4, 5)))


def asd():
    a = 1
    print(globals() == locals())
    print(globals())
    print(locals())


print(max(1, 2, 3, 4))
print(dir(object))


hi = [2, 3, 123, 67, -23, -67]
print(sorted(hi, reverse=True))


# def sum_range(start, end):
#     return sum(range(start, end+1)) if end > start else sum(range(end, start+1))


def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end+1))


print(sum_range(3, 1))


rock = 8


def inner():
    global rock
    rock+=1
    return rock


print(inner())


# def three_args(*, var1, var2=None, var3=None):
#     arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
#     print(f'Переданы аргументы: {arguments}')


def three_args(*, var1, var2=None, var3=None):
    arguments = ''.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Arguments: {arguments}')


three_args(var1=21)
three_args(var1='Python', var3=3)
three_args(var1='Python', var2=3, var3=9)

#
# from datetime import datetime
# from time import sleep
#
#
# def time_now(msg, *, dt=None):
#     if dt is None:
#         dt = datetime.now()
#     print(msg, dt)
#
#
# # Тесты
# time_now('Сейчас такое время: ')
# sleep(1)
# time_now('Прошла секунда: ')
# sleep(1)
# time_now('Ничего не понимаю... ')
#
#


import inspect


# def inspect_function(func):
#     f = func
#     name = f.__name__
#     param = inspect.getfullargspec(func)
#     context = {
#         "name": name,
#         "param": param
#     }
#     return context
#
#
# def nam(a, e):
#     pass
#
#
# print(inspect_function(nam))

import math


def inspect_function(some_func):
    print(f'Анализируем функцию {some_func.__name__}')
    for param in inspect.signature(some_func).parameters.values():
        print(param.name, param.kind, sep=': ')


# Некая функция для анализа
def my_func(a, b, /, c, d, *args, e, f, **kwargs):
    pass


# Тесты
inspect_function(my_func)
print('-' * 25)
inspect_function(math.sqrt)

#
# def pack(**kwargs):
#     print(kwargs)
#
#     def inner_pack():
#         nonlocal kwargs
#         arg1, arg2 = kwargs.items()
#         kwargs.update(dict(key3=4, key4=6))
#         print(kwargs)
#         print(arg1, arg2)
#
#     inner_pack()
#
#
# pack(key1=2, key2=3)


def sub_set(set_):
    all_sub_set = []
    list_set = list(set_)
    inner_lst = []
    goal = []
    for x in list_set:
        lst = []

        def sub_set_inner():
            inner_lst.append(x)
            kitten = inner_lst[:]
            for k in inner_lst:

                kitten= [x]
                kitten.append(k)
                print(kitten)
                # print(inner_lst[k-1:len(inner_lst)])
                # for i in inner_lst[k-1:]:
                #     kitten = []
                #     kitten.extend(inner_lst)
                #     # print(kitten)
                #     kitten.append(k)
                #     goal.append(kitten)
                #     # print(i)
                # print('sid')
        sub_set_inner()




    # i = 2
    # for d in list_set:
    #     for x in list_set:
    #         new_list = []
    #         for k in list_set[d-1:i]:
    #             new_list.append(k)
    #         all_sub_set.append(tuple(new_list))
    #         i += 1
    #         print(x)
    #     print(set(all_sub_set))
    # list_set.reverse()
    # for d in list_set:
    #     for x in list_set:
    #         new_list = []
    #         for k in list_set[d-1:i]:
    #             new_list.append(k)
    #         all_sub_set.append(tuple(new_list))
    #         i += 1
    #         print(x)
    # d = set(all_sub_set)
    # print(d)


sub_set({1,2 ,3})


new_array=[1,2,3,4]
power_set=[[]]
for x in new_array:
    print(power_set)
    for i in range(len(power_set)):
        tmp_list = power_set[i].copy()
        tmp_list.append(x)
        power_set.append(tmp_list)
print(power_set)


