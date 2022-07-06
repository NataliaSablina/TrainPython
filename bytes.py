from figure import square_perimetr

print(square_perimetr())


empty_bytes = bytes(4)
print(empty_bytes)
print(type(empty_bytes))


data_bytes = bytes(b'\xFF\xFF')
print(data_bytes)

mutable_bytes = bytearray(b'\xFF\xFF\xAB\xAB')
print(id(mutable_bytes))
mutable_bytes[0] = 2
mutable_bytes.append(255)
print(id(mutable_bytes))
print(mutable_bytes)
print(type(mutable_bytes))

print(min(mutable_bytes))
print(max(mutable_bytes))

try:
    print(mutable_bytes.index(255))
except ValueError:
    print('No one')

print(mutable_bytes.count(255))

print(255 in mutable_bytes)

mutable_bytes2 = bytearray(b'\xAF\x34')
print(id(mutable_bytes))
print(id(mutable_bytes2))
print(id(mutable_bytes + mutable_bytes2))
print(mutable_bytes + mutable_bytes2)
print(id(mutable_bytes + mutable_bytes2))
print(mutable_bytes*3)
print(mutable_bytes)

print(mutable_bytes[3])
print(mutable_bytes[1:3])
print(mutable_bytes[1:4:2])

print(len(mutable_bytes))

mutable_bytes3 = bytearray(b'\xd0\x9f\xd0\xb4\xd0\xb9')
print(mutable_bytes3.count(255, 0, 5))
print(b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8'))
print(b'\xd0\x9f\xd0\xb4\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8'))
print(mutable_bytes3.decode('utf-8'))
print(mutable_bytes3.endswith(b'\xb9'))
print(mutable_bytes3.maketrans(b'\xff', b'\xff'))
