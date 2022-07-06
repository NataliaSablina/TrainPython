import re


def simplify(poly):
    pol = list(poly)
    mono = []
    insects = "-+/*"
    mono2 = []
    t = 0
    for i in pol:
        print(i)
        if i not in insects:
            mono.append(i)
            t += 1
            print(mono)
        else:
            str_help = ''.join(mono[0:t])
            mono2.append(str_help)
            mono2.append(i)
            continue
        print(8)

    print(mono2)


simplify('2xy-yx')
