'''method chaining'''


class multipp:
    def de(self, a):
        print("inside de")
        print(a)
        return self

    def ce(self, b):
        print("inside ce")
        print(b)
        return self


mul = multipp()
mul.de(4).ce(6)
'''fn chaining'''


def f1(a):
    def f2(b):
        return a * b

    return f2


c = f1(6)
print(c(5))
