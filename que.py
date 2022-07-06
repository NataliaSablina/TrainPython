from collections import deque
from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 'Apple'))
q.put((1, 'Banana'))
q.put((3, 'Mango'))

while not q.empty():
    next_item = q.get()
    print(next_item)

pri_que = []

pri_que.append((2, 'Apple'))
pri_que.append((1, 'Mango'))
pri_que.append((3, 'Banana'))

# NOTE: Remember to re-sort every time
#       a new element is inserted.
pri_que.sort(reverse=True)

while pri_que:
    next_item = pri_que.pop()
    print(next_item)


class Queue1:
    def __init__(self):
        self.__queue = list()

    def add_element(self, value):
        if value not in self.__queue:
            self.__queue.append(value)
            return True
        else:
            self.__queue.append(value)
            return False

    def remove_element(self):
        if self.qsize() > 0:
            return self.__queue.pop(0)
        else:
            return f"Your Queue is empty"

    def qsize(self):
        return len(self.__queue)

    def __str__(self):
        return f"{self.__queue}"

    def empty(self):
        if self.qsize()==0:
            return True
        else:
            return False


queue2 = Queue1()
queue2.add_element(2)
queue2.add_element(3)
queue2.add_element(4)
queue2.add_element(3)

print(queue2)

print(queue2.remove_element())
print(queue2.remove_element())
print(queue2.remove_element())
print(queue2.remove_element())

print(queue2.empty())

from collections import deque

que = deque()

que.append('Apple')
que.append('Mango')
que.append('Banana')

print(que)
deque(['Apple ', 'Mango', 'Banana'])

print(que.popleft())

print(que.popleft())


class PriorityQueue:
    pass