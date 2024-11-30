class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Cat(metaclass=Singleton):

    def __init__(self, color):
        self.color = color


class Test(metaclass=Singleton):
    global_field = 42


black_cat = Cat("black")
white_cat = Cat("white")
assert black_cat is white_cat
print(Test.global_field)

