import operator
import re

#
# def top_3_words(text):
#     text_2 = text.lower()
#     words_list = re.split("/|-|,|#|@|!|&|\.|\?|\{|}|\s|:|;|_|\s\s", text_2)
#     myString = ' '.join(words_list)
#     text = text.replace(\s{2,}/g, ' ')
#     return myString
#     # words = {}
#     # for word in words_list:
#     #     print(words_list.count(word), word)
#     #     words[word] = words_list.count(word)
#     # d = {'b': 9, 'a': 3, 'c': 7}
#     # sorted_tuple = dict(sorted(words.items(), key=lambda x: x[1]))
#     # word_list = []
#     # for word in sorted_tuple:
#     #     word_list.append(word)
#     # word_list.reverse()
#     # if len(word_list)<=3:
#     #     return
#     # return word_list[:3]
#
#
#
# # /|?|.|}|{|]|[|=|-|_|+|@|.|,|!|^|$|;|:&|
# # text = "sss aaaaaaaaaaaaaaaaaa/ffffffffff.eeeee?eeeeeee&fdfdd{cdvdv dsvsd}v v v v sss sss sss sss SSS"
# text ="""В деревушке Ла-Манча, название которой у меня нет желания называть
# заметьте, не так давно жил один из тех джентльменов, которые держат копье
# в стойке для копий старый щит, худощавый кляч и борзая для
# курсирование. Олла скорее из говядины, чем из баранины, салат на большинстве
# ночи, объедки по субботам, чечевица по пятницам и голубь или около того дополнительно
# по воскресеньям забрал три четверти своего дохода"""
# print(top_3_words(text))
#
# import re
#
# a = """В деревушке Ла-Манча, название которой у меня нет желания называть
# заметьте, не так давно жил один из тех джентльменов, которые держат копье
# в стойке для копий старый щит, худощавый кляч и борзая для
# курсирование. Олла скорее из говядины, чем из баранины, салат на большинстве
# ночи, объедки по субботам, чечевица по пятницам и голубь или около того дополнительно
# по воскресеньям забрал три четверти своего дохода"""
# res = ' '.join(sorted(a.split(), key=lambda x: int(re.sub(r'.*?(\d+).*', r'\1', x+'_99999'))))
# print(res)

a = [4, 6, 7]
print(min(a))


import re


def top_3_words(str):
    text_lower = str.lower()
    words_list_1 = re.split("/|-|,|#|@|!|&|\.|\?|\{|}|\s|:|;|_|\s\s", text_lower)
    myString = ' '.join(words_list_1)
    t = re.sub(r'[^\w\s\']+', '', myString)
    if len(t) > 0 and t.count("""'""") / len(t) >= 0.20:
        return []
    words_list = t.split()
    words_dict = dict()
    for word in words_list:
        num = words_list.count(word)
        words_dict.update({word: num})
    sorted_words = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))
    if len(sorted_words.keys()) >= 3:
        top_words = list(sorted_words.keys())[0:3]
        return top_words
    if len(sorted_words.keys()) < 3:
        top_words = list(sorted_words.keys())
        return top_words




a = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old bu'ckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""
print(top_3_words(" ' "))

res = ' '.join(sorted(a.split(), key=lambda x: int(re.sub(r'.*?(\d+).*', r'\1', x+'_99999'))))
print(res)