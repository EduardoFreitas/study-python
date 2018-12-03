class Calculator:

    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b

    def sum_up_method(self):
        return self._a + self._b

    @classmethod
    def sum_up_class_method(cls, a, b):
        return cls(a, b)

    @staticmethod
    def sum_up_static(a, b):
        return a + b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

# new instance
calc_1 = Calculator(1, 1)

# call method
print(calc_1.sum_up_method())
# call classmethod
calc_2 = calc_1.sum_up_class_method(2, 2)
# call method for the result
print(calc_2.sum_up_method())
# call static method
print(calc_1.sum_up_static(4, 4))

# Testing property
print(calc_1.a)
calc_1.a = 3
print(calc_1.a)

