def digitize(n):
    num_lst = []
    num_lst.extend(str(n)[::-1])
    num_lst2 = []
    for el in num_lst:
        num_lst2.append(int(el))
    return num_lst2


#
# def digitize(n):
#     return map(int, str(n)[::-1])


number = 123456789
print(digitize(number))


def row_sum_odd_numbers(k):
    n = []
    num = 1
    iter = 2
    a = []

    for i in range(9):
        for j in range(9):
            if i >= j:
                a.append(num)
                num2 = num
                print(num2)
                c = num2
                num = c
                num += iter
            else:
                a.append(0)
        n.append(a)

    b = n[0]
    list_chop = [[b[x], b[x + 1], b[x + 2], b[x + 3], b[x + 4], b[x + 5], b[x + 6], b[x + 7], b[x + 8]] for x in
                 range(0, len(b), 9)]
    print(list_chop)
    return sum(list_chop[k - 1])


def row_sum_odd_numbers(n):
    # your code here
    return n ** 3


print(row_sum_odd_numbers(9))


# n = []
# num = 1
# iter = 2
# column = 1
# a = []
#
# for i in range(9):
#     for j in range(9):
#         if i >= j:
#             a.append(num)
#             num2 = num
#             print(num2)
#             c = num2
#             num = c
#             num += iter
#         else:
#             a.append(0)
#     n.append(a)
#
# print(n)
#
#
#


def dig_pow(n, p):
    list_of_str_numbers = list(str(n))
    result = 0
    while list_of_str_numbers:
        digit = int(list_of_str_numbers.pop(0))
        result += pow(digit, p)
        p += 1
    if result % n == 0:
        return result / n
    else:
        return -1


print(dig_pow(92, 1))


def series_sum(n):
    numerator = 1
    denominator = 1
    i = 0
    result = 0
    while i != n:
        result += numerator / denominator
        denominator += 3
        i += 1
    if n == 0:
        return "%.2f" % round(0, 2)
    return "%.2f" % round(result, 2)


print(series_sum(0))


def func_sort(x):
    if x % 2 != 0:
        return x
    else:
        return x + 100


def sort_array(source_array):
    pass


lst = [5, 8, 6, 3, 4]


def my_sort(a):
    temp = []
    for i in range(len(a)):
        if a[i] % 2 != 0:
            temp.append(a[i])
            a[i] = " "

    temp.sort(reverse=True)  # сортировка в обратном порядке

    for i in range(len(a)):
        if a[i] == ' ':
            a[i] = temp.pop()
    return a


print(my_sort(lst))

# [-1, 150, 160, 170, -1, -1, 180, 190]
