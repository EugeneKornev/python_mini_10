def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class Cat:
    def __init__(self, color):  # :)
        self.color = color


my_cat = Cat('black')
friends_cat = Cat('white')
print(id(my_cat) == id(friends_cat))

