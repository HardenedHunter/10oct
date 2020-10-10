def add1(x, y):
    return x + y


class Adder:
    value = 10

    def __call__(self, x, y):
        return x + y

    @classmethod
    def my_method(cls):
        print('Hello', cls.value)


add2 = Adder()
print(add2.value)
add3 = Adder()
Adder.value = 55
print(add2.value)
# print(add1(10, 20))
# print(add2(10, 20))
