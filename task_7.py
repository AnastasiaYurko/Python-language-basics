class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        c_1 = self.a + other.a
        c_2 = self.b + other.b
        return ComplexNumber(c_1, c_2)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b,
                             self.a * other.a + self.b * other.b)


com_num_1 = ComplexNumber(1, 2)
com_num_2 = ComplexNumber(3, 4)
com_num_3 = com_num_2 + com_num_1
com_num_4 = com_num_2 * com_num_1
print(f'Комплексное число 1: {com_num_1}')
print(f'Комплексное число 2: {com_num_2}')
print(f'Сумма комлексных чисел 1 и 2: {com_num_3}')
print(f'Произведение комплексных чисел 1 и 2: {com_num_4}')
