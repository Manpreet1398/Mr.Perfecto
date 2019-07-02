class overlaod:
    def __init__(self, a):
        self.a = a

    def __add__(self, b):
        return self.a + b.a

    def __mul__(self, c):
        return self.a * b.a

    def __gt__(self, d):
        if (self.a > d.a):
            return True
        else:
            return False

    def __lt__(self, d):
        if (self.a < d.a):
            return True
        else:
            return False

    def __eq__(self, d):
        if (self.a == d.a):
            return True
        else:
            return False


a = overlaod(4)
b = overlaod(6)
d = overlaod(7)

print(a + b)
print(a * b)
print(a > d)
print(a < d)
print(a == d)
