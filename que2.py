import math
from queue import Queue


class Queue1:
    def __init__(self):
        self.__queue = []

    def push(self, value):
        if value not in self.__queue:
            self.__queue.append(value)
            return True
        else:
            self.__queue.append(value)
            return False

    def get(self):
        if self.qsize() > 0:
            return self.__queue.pop(0)
        else:
            return f"Your Queue is empty"

    def qsize(self):
        return len(self.__queue)

    def __str__(self):
        return f"{self.__queue}"

    def empty(self):
        if self.qsize() == 0:
            return True
        else:
            return False

    def reverse(self):
        self.__queue.reverse()
        return self.__queue

    def reverse_k(self, k: int):
        part_1 = self.__queue[:len(self.__queue) - k:]
        part_2 = self.__queue[len(self.__queue) - k::]
        part_2.reverse()
        part_1.extend(part_2)
        self.__queue = part_1
        return self.__queue


q = Queue1()
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.push(6)
q.push(7)
q.push(8)
print(q)
print(q.get())

# k = int(input(f"Введите , сколько элементов в очереди надо обернуть"))
k = 3
print(q.reverse_k(k))


class Stack:
    def __init__(self):
        self.__stack__ = Queue1()

    def push(self, value):

        self.__stack__.push(value)

        return True

    def get(self):
        if self.stack_size() > 0:
            self.__stack__.reverse()
            a = self.__stack__.get()
            self.__stack__.reverse()
            return a
        else:
            return f"Your Queue is empty"

    def stack_size(self):
        return self.__stack__.qsize()

    def __str__(self):
        return f"{self.__stack__}"

    def reverse(self):
        self.__stack__.reverse()
        return self.__stack__


#
# stack = Stack()
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# print(stack)
# print(stack.get())
# print(stack)


class Queue2:
    def __init__(self):
        self.__queue_main__ = Stack()

    def push(self, value):
        self.__queue_main__.push(value)
        return True

    def get(self):
        self.__queue_main__.reverse()
        a = self.__queue_main__.get()
        self.__queue_main__.reverse()
        return a

    def __str__(self):
        return f"{self.__queue_main__}"


q2 = Queue2()
q2.push(2)
q2.push(3)
q2.push(4)
q2.push(5)
print(q2)
print(q2.get())


#
# class Stack2:
#     def __init__(self):
#         self.stack = []
#
#     def __bool__(self):
#         return bool(self.stack)
#
#     def push(self, elem):
#         if self.stack:
#             self.stack.append((elem, min(elem, self.stack[-1][1])))
#         else:
#             self.stack.append((elem, elem))
#
#     def pop(self):
#         return self.stack.pop()[0]
#
#     def get_min(self):
#         if not self.stack:
#             return math.inf
#         return self.stack[-1][1]
#
#
# class Queue3:
#     def __init__(self):
#         self.s1 = Stack2()
#         self.s2 = Stack2()
#
#     def push(self, elem):
#         self.s1.push(elem)
#
#     def pop(self):
#         if not self.s2:
#             while self.s1:
#                 self.s2.push(self.s1.pop())
#         return self.s2.pop()
#
#     def get_min(self):
#         return min(self.s1.get_min(), self.s2.get_min())


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr[0]


arr = [3, 1, 2, 5, 4]
print(selection_sort(arr))


def min(list):
    stack_2 = Stack()
    stack_3 = Stack()
    for i in list:
        stack_2.push(i)
    min = int(stack_2.get())
    stack_3.push(min)
    while stack_2.stack_size() > 0:
        a_2 = int(stack_2.get())
        if min <= a_2:
            stack_3.push(a_2)
        else:
            stack_3.reverse()
            stack_3.push(a_2)
            stack_3.reverse()
            print(f'{stack_3}')
        stack_3.reverse()
        min = stack_3.get()
        stack_3.push(min)
        stack_3.reverse()
    stack_3.reverse()
    return stack_3.get()


print('ddddddddddddddddd')
print(min([1, 2, -3, -1, -2, 8, 9, -4, 1, -99, 4, 0, 5]))
