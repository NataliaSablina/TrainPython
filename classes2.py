class Animal:
    def say(self):
        raise NotImplementedError("Метод say() обязательно должен быть переопределен в дочернем классе")


class Dog(Animal):
    def say(self):
        print("AF")


class Cat(Animal):
    def say(self):
        print("Myu")


class Fox(Animal):
    def say(self):
        print("SHHH")


d = Dog()
c = Cat()
f = Fox()
animal = []
animal.append(d)
animal.append(c)
animal.append(f)

for a in animal:
    a.say()


class Table:
    def __init__(self):
        pass


class RectangleTable(Table):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def size(self):
        return self.__width * self.__height


class RoundTable(Table):
    def __init__(self, rad):
        super().__init__()
        self.__rad = rad

    def size(self):
        return 3.14*pow(self.__rad, 2)


rec = RectangleTable(9, 4)
round = RoundTable(5)
print(rec.size(), round.size())
