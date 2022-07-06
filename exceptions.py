# try:
#     print('FFFFFFFFF')
# except Exception as e:
#     print(e)
# else:
#     print("File was readed")
#
# try:
#     raise Exception("Some exception")
# except Exception as e:
#     print("Exception exception " + str(e))
#
#
# class NegValException(Exception):
#     pass
#
#
# try:
#     val = int(input("input positive number: "))
#     if val < 0:
#         raise NegValException("Neg val: " + str(val))
#     print(val + 10)
# except NegValException as e:
#     print(e)


# class MyCustomError(Exception):
#     def __init__(self, *args):
#         if args:
#             self.message = args[0]
#         else:
#             self.message = None
#
#     def __str__(self):
#         print("Calling str")
#         if self.message:
#             return 'MyCustomError, {0}'.format(self.message)
#         else:
#             return 'Raised MyCustomError'
#
#
# raise MyCustomError('hello')
#
#
#

class ListElementIntFloatError(Exception):

    def __init__(self, *args):
        if str is not None:
            self.message = args[0]
        else:
            self.message

    def __str__(self):
        if self.message:
            return 'ListElementIntFloatError has been raised, {0}'.format(self.message)
        else:
            return ('ListElementIntFloatError has been raised')


class CustomList(list):

    def __init__(self, *args):
        self.empty_list = []
        if args is None:
            self.get_list()
        for elem in args:
            if isinstance(elem, (int, float)):
                self.empty_list.append(elem)
            else:
                type_elem = type(elem)
                raise ListElementIntFloatError('You should enter "int" or "float" not {0}'.format(type_elem.__name__))

    def get_list(self):
        return self.empty_list

    def add(self, number):
        if isinstance(number, (int, float)):
            self.empty_list.append(number)
        else:
            type_elem = type(number)
            raise ListElementIntFloatError('You should enter "int" or "float" not {0}'.format(type_elem))


try:
    number_list = CustomList(1, '999')
    print(number_list.get_list())
except ListElementIntFloatError as error:
    print(error)


try:
    a = 10/0
except ZeroDivisionError as z:
    print(z)
else:
    print(a)
finally:
    print("End")
