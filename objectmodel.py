# def my_function(val):
#     b = val[:2]
#     c = val[2:]
#     return b, c
#
#
# a = [1, 2, 3, 4, 5]
# first, second = my_function(a)
# print(first)
# print(second)

# a, b, *c = [1, 2, 3, 4, 5]
# def test(first, second, *a):
#     for item in a:
#         print(item)
# test(1, 2, 3, 4, 5)

# str(p1)  ->    __str__
# len(p1)  ->    __len__
# Cls(...) ->    __init__
# p1 + p2  ->    __add__
# p1()     ->    __call__

class Polynomial:
    def __init__(self, *coeffs):
        self.__coeffs = coeffs

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        return f'Polynomial{self.__coeffs}'

    def __len__(self):
        return len(self.__coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.__coeffs, other.__coeffs)))

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    # greater than or equal to
    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def my_method(self):
        pass


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(1, 2, 3)
print(p1 == p2)

