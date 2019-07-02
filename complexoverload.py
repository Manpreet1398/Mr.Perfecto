class vector:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        if not isinstance(other, vector):
            return NotImplemented
        return vector([a + b for a, b in zip(self.num, other.num)])

    def __mul__(self, other):
        if not isinstance(other, vector):
            return NotImplemented
        return vector([a * b for a, b in zip(self.num, other.num)])

    def __str__(self):
        return ','.join(map(str, self.num))


a = vector([1, 2, 3])
b = vector([9, 10, 12])
print(a + b)
print(a * b)


class mulvector:
    def __init__(self, num):
        self.num = num

    def __mul__(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            return NotImplemented
        return mulvector([a * other for a in self.num])

    def __str__(self):
        return ','.join(map(str, self.num))


a = mulvector([1, 2, 3])
print(a * 2)
