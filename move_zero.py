def move_zeros(array):
    zero_num = 0
    for el in array:
        index = array.index(el)
        deleted = array.pop(index)
        if deleted == 0:
            zero_num += 1
        else:
            array.insert(index, deleted)
    for i in range(zero_num):
        array.append(0)
    return array


lst = [0, 2, 0]
print(move_zeros(lst))
