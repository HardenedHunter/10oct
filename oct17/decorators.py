# for i in range(10):
#     class Person:
#         def __init__(self, age):
#             self.age = age
#
#         def __str__(self):
#             return f'Person({self.age})'
#
# p = Person(10)
# print(p)

from time import time, sleep


def timer(func):
    def inner(*args, **kwargs):
        begin = time()
        sleep(2)
        result = func(*args, **kwargs)
        print(f'Прошло: {time() - begin} в функции {func.__name__}')
        return result
    return inner


def ntimes(n):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = 0
            for i in range(n):
                print(f'Выполняется {func.__name__}')
                result = func(*args, **kwargs)
            return result
        return inner
    return wrapper


@timer
def mult(x, y=10):
    return x * y

@timer
def add(x, y):
    return x + y


@ntimes(10)
def sqr(x):
    return x ** 2


logged_in = True


def auth_required(func):
    def inner(user_id):
        if logged_in:
            return func(user_id)
        return 'redirected to login page'
    return inner


@auth_required
def get_user_profile(user_id):
    print('Querying the database....')
    return f'Some user with id: {user_id}'


print(get_user_profile(77612319))
