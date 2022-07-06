def polindrom(str_):
    str_.lower()
    if str_ == ''.join(list(reversed(list(str_)))):
        return True
    return False


print(polindrom('aaa'))


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


def delete_indications(str_):
    list_str = []
    for el in str_:
        if el not in punctuations:
            list_str.append(el)
    return ''.join(list_str)


my_str = "Привет!!!, Меня зовут ---Алексей."
print(delete_indications(my_str))


def alphabet(str_):
    lst = str_.split()
    lst.sort()
    return lst


my_str = "Привет, это пример строки в алфавитном порядке"
words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
   print(word)


strin = "99"
count = 0
for i in strin:
    count+=1

print(count)


glasalph = 'аеёиоуэюя'

ip_str = 'Привет, меня зовут Тимур, мне 30 лет, в этом предложении, мы будет считать количество глассных букв?'

ip_str = ip_str.casefold()

count = {}.fromkeys(glasalph,0)

for char in ip_str:
   if char in count:
       count[char] += 1

print(count)


str1 = "Игра"
str2 = "Рига"

# Приводим в нижний регистр
str1 = str1.lower()
str2 = str2.lower()

if len(str1) == len(str2):
    # Сортируем обе строки
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if (sorted_str1 == sorted_str2):
        print(str1 + " и " + str2 + " Являются анаграмой.")
    else:
        print(str1 + " и " + str2 + " не являются анаграмой.")

else:
    print(str1 + " и " + str2 + " не являются анаграмой")



