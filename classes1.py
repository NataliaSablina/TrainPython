class Point3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


pt1 = Point3D()
pt1.msg = 9
print(pt1.msg)
pt1.x = 5
pt1.y = 8
pt1.z = 6
print(pt1.__dict__)
pt1.__setattr__("play", 2)
print(pt1.__dict__)
pt1.__delattr__("play")
pt1.__delattr__("msg")
print(hasattr(pt1, "msg"))
print(pt1.__dict__)
pt2 = Point3D()
print(pt1.__dict__)
print(pt2.z)
pt2.z = 5
print(pt2.__dict__)


class Point2D:
    __x = 0
    __y = 0
    coords = [__x, __y]

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y
        self.coords = [self.__x, self.__y]

    def get_coords(self):
        return tuple(self.coords)


pt = Point2D()
pt.set_coords(2, 3)
print(pt.get_coords())


class Point:
    x = 0
    y = 0

    def __init__(self, other=None):
        if other:
            self.x = other.x
            self.y = other.y


point1 = Point()
point1.x = 9
point1.y = 8
print(point1.x, point1.y)
point2 = Point(point1)


#
# print(dir(point1))
# point3D_list = []
# i = 0
# while i != 5:
#     x = int(input("Enter x:"))
#     y = int(input("Enter y:"))
#     z = int(input("Enter z:"))
#     point = Point3D(x, y, z)
#     point3D_list.append(point)
#     i+=1
#
#
# for point in point3D_list:
#     print(point.x, point.y, point.z)


class P:
    WIDTH = 50

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    #
    # def __getattribute__(self, item):
    #     if item == "_P__x" or item == "_P__y":
    #         return "Yes"
    #     else:
    #         return object.__getattribute__(self, item)
    #
    # def __setattr__(self, key, value):
    #     if key == "WIDTH":
    #         raise AttributeError
    #     else:
    #         self.__dict__[key] = value
    #         # self.__x = value  #нельзя тк по рекурсии будет вызывать метод __setattr__
    #
    # def __getattr__(self, item):
    #     return print("__getattr__: " + item)
    #
    # def __delattr__(self, item):
    #     return print("__delattr__: " + item)

    @property
    def getCoord(self):
        return self.__x, self.__y

    @getCoord.setter
    def getCoord(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @getCoord.deleter
    def getCoord(self):
        print("Del")
        del self.__x


pnt = P(1, 2)
print(pnt.getCoord)
pnt.getCoord = 4, 5
print(pnt.getCoord)
del pnt.getCoord


class NoData:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return "_NoData__name"


class CoordValue:
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    # def __delete__(self, obj):
    #     del self.__value


class Point1:
    coordX = CoordValue()
    coordY = CoordValue()
    noData = NoData()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


p = Point1(1, 2)
p.coordX = 7
print(p.coordX, p.coordY)
p2 = Point1(4, 5)
print(p2.coordX, p2.coordY)
p2.noData = "hello"


class DataException(Exception):

    def __init__(self, message=None):
        if message:
            self.message = message
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'


class Calender:
    __slots__ = ["day", "month", "year"]

    def __init__(self, day="1", month="1", year="1"):
        Calender.__check_data(day, month, year)
        self.day = day
        self.month = month
        self.year = year

    def __check_data(day, month, year):
        if isinstance(day, str) and isinstance(month, str) and isinstance(year, str):
            try:
                day = int(day)
                month = int(month)
                year = int(year)
            except ValueError:
                print("Все данные должны быть представлены ввиде целых чисел")
                exit(0)
            else:
                if day < 0 or day > 31:
                    raise DataException("Значение дня должно быть в диапозоне от 0 до 31")
                if month < 0 or month > 12:
                    raise DataException("Значение месяца должно быть в диапозоне от 0 до 12")
                if year < 0:
                    raise DataException("Значение года должно быть больше 0")
                return True
        return False

    def get_data(self):
        return f'{self.day}.{self.month}.{self.year}'


cal = Calender("3", "11", "2000")
print(cal.get_data())


class Coords:
    def __set_name__(self, owner, name):
        print("___________________________name")
        self.__name = name

    def __get__(self, instance, owner):
        print("___________________________get")
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        print("___________________________set")
        instance.__dict__[self.__name] = value


class Rectangle:
    __left__upper_x = Coords()
    __left__upper_y = Coords()
    __right__lower_x = Coords()
    __right__lower_y = Coords()

    def __init__(self, left__upper_x=0, left__upper_y=0, right__lower_x=0, right__lower_y=0):
        for i in [left__upper_x, left__upper_y, right__lower_x, right__lower_y]:
            if Rectangle.__validator(i):
                self.__left__upper_x = left__upper_x
                self.__left__upper_y = left__upper_y
                self.__right__lower_x = right__lower_x
                self.__right__lower_y = right__lower_y
            else:
                return f"Все значения должны быть int или float"

    def __validator(param):
        return isinstance(param, (int, float))

    def getCoords(self):
        return self.__left__upper_x, self.__left__upper_y, self.__right__lower_x, self.__right__lower_y

    def setCoords(self, left_upper_x, left_upper_y, right_lower_x, right_lower_y):
        for i in [left_upper_x, left_upper_y, right_lower_x, right_lower_y]:
            if Rectangle.__validator(i):
                self.__left__upper_x = left_upper_x
                self.__left__upper_y = left_upper_y
                self.__right__lower_x = right_lower_x
                self.__right__lower_y = right_lower_y
            else:
                print("Wrong input! (Excpected int/float)")


rec = Rectangle(1, 2, 3, 4)
print(rec.getCoords())
rec.setCoords(9, 7, 6, 5)
print(rec.getCoords())
rec.setCoords(0, 0, 7, 8)
print(rec.getCoords())


class G:
    x = 0


g1 = G()
g2 = G()
print(g1.x, g2.x)
g1.x = 9
print(g1.x, g2.x)
G.x = 10
print(g1.x, g2.x)


class ABC:
    __instance = None
    __count = 0

    def __new__(cls, *args, **kwargs):  # выполняется перед тем как создать экземпляр класса, в этом
        # методе и создается экземпляр и мы перегружая #
        # его можем контролировать сколько раз он создастся
        #cls - ссылается на этот класс
        #недостаток этого способа реализации синглтона - от наследников можно создать новые экземпляры этого класса
        if not isinstance(ABC.__instance, cls):
            cls.__instance = super(ABC, cls).__new__(cls) #присваиваем ссылку свойству cls.__instance
        else:
            print("Экземпляр класса АВС уже создан!")

    def __init__(self, x=0, y=0):
        ABC.__count += 1
        self.coordX = x
        self.coordY = y


a = ABC()
b = ABC()
d = ABC()
print(id(a), id(b), id(d)) #id ссылаются на один и тот же объект тк новых ссылок не создавалось


class Rectangle2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.square = Rectangle2.__get_square(self.x, self.y)

    @staticmethod
    def __get_square(x, y):
        return x*y


u = Rectangle2(3, 4)
print(u.x, u.y, u.square)


class Dog:
    __count = 0

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        if not cls.__count > 5:
            print("IIIIIIIIIIIIIIIIIIIIII")
            super(Dog, cls).__new__(cls)
        else:
            print("You can create 5 dogs maximum")

    def __init__(self, name="Spot", age=18, race="Usual"):
        self.name = name
        self.age = age
        self.race = race


d1 = Dog()
d2 = Dog()
d3 = Dog()
d4 = Dog()
d5 = Dog()
d6 = Dog()


class PersonalComputer:
    def __init__(self, memory_size=0, disk="Rude", cpu=0):
        self.memory_size = memory_size
        self.disk = disk
        self.cpu = cpu


class TablePK(PersonalComputer):
    def __init__(self, memory_size=0, disk="Rude", cpu=0, monitor="Pixel", klava="Pixel"):
        super().__init__(memory_size=0, disk="Rude", cpu=0)
        self.monitor = monitor
        self.klava = klava

    def get_info(self):
        return self.memory_size,  self.disk, self.cpu, self.monitor, self.klava


class LapTop(PersonalComputer):
    def __init__(self, memory_size=0, disk="Rude", cpu=0, diagonal=30):
        super().__init__(memory_size, disk, cpu)
        self.diagonal = diagonal

    def get_info(self):
        return self.memory_size,  self.disk, self.cpu, self.diagonal


pk = PersonalComputer()
lt = LapTop()
print(lt.get_info())
tb = TablePK()
print(tb.get_info())
