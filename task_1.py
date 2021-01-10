class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        new_matrix = []

        for i in zip(self.matrix, other.matrix):
            new_matrix.append([sum([j, k]) for j, k in zip(*i)])

        return Matrix(new_matrix)


m = Matrix([[3, 4, 5], [2, 4, 6], [85, 76, 20]])
m_1 = Matrix([[4, 5, 8], [9, 12, 15], [9, 10, 25]])
print(m + m_1)
