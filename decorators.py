import time
import functools


def pets(master, *pets):
    for pet in pets:
        print(f"{master}, {pet}")


pets("John", "cat", "dog")


def animals(**pets):
    for name, pet in pets.items():
        print(f"{pet} : {name}")


animals(cat=["Mike", "John"], dog="Travias")


def retry(max_retries):
    def retry_decorator(func):
        def _wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except:
                    time.sleep(1)

        return _wrapper

    return retry_decorator


@retry(1)
def might_fail():
    print("might_fail")
    raise Exception


might_fail()


def retry(func):
    def _wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            print("Exception")
            time.sleep(1)
            try:
                func(*args, **kwargs)
            except Exception:
                print("Exception")
        finally:
            print("finally code")

    return _wrapper


@retry
def might_fail():
    print("might_fail")
    raise Exception


might_fail()


def two(func):
    def wrapp(*args, **kwargs):
        start_time = time.perf_counter_ns()
        umn = func(*args, **kwargs)
        print(f"{time.perf_counter_ns() - start_time} ns")
        return 2 * umn

    return wrapp


@two
def calc(a, b):
    return a * b


a = 2
b = 3
print(calc(a, b))


def logit(func):
    # "@functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        arg = args
        kwarg = kwargs
        return print(f"Function was called with {arg} and {kwarg}")
    return wrapper


@logit
def mal(a, b):
    return a+b

mal(2,3)


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        start_time2 = time.perf_counter_ns()
        func(*args, **kwargs)
        end_time2 = time.perf_counter_ns()
        return print(func.__name__ + f" {end_time-start_time} ns {end_time2-start_time2} ns" + f" {func(*args, **kwargs)}")
    return wrapper


@logit
@timer
def trader(a, b):
    return a*b


trader(3, 6)


class MyDecorator:
    def __init__(self, function):
        self.function = function
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)
        self.counter += 1
        print(f"Called {self.counter} times with args{args}")


@MyDecorator
def hire(a:int):
    return a


hire(8)
hire(6)
hire(9)


def add_calc(cls):

    def hire(self):
        return 4

    cls.hire = hire
    return cls


@add_calc
class Div:
    def __init__(self):
        print("MyClass __init__")


my_obj = Div()
print(my_obj.hire())


class MyClass:
    def __init__(self, x):
        self.x = x

    @property
    def x_doubled(self):
        return self.x * 2

    @x_doubled.setter
    def x_doubled(self, x_doubled):
        self.x = x_doubled // 2


my_object = MyClass(5)
print(my_object.x_doubled)  # 10
print(my_object.x)  # 5
my_object.x_doubled = 100  #
print(my_object.x_doubled)  # 100
print(my_object.x)


"""
Ещё один широко известный декоратор — это @staticmethod. 
Он используется в ситуациях, когда надо вызвать функцию, 
объявленную в классе, не создавая при этом экземпляр дан"""

set2 = {1, 2, 3};
print(set2, id(set))
set2.add(7)
print(set2, id(set))




















