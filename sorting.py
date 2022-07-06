from random import randint


# bubble sorting

N = 10
a = []

for i in range(N):
    a.append(randint(1, 99))

print(a)

for i in range(N - 1):
    for j in range(N - i -1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)


bubble_list = []

for i in range(1, 100):
    bubble_list.append(randint(1, 1000))

print(bubble_list)


for i in range(len(bubble_list) - 1):
    for j in range(len(bubble_list)-i-1):
        if bubble_list[j] > bubble_list[j+1]:
            bubble_list[j], bubble_list[j+1] = bubble_list[j+1], bubble_list[j]

print(bubble_list)
