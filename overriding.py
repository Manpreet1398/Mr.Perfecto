# overriding
class over:
    def __init__(self, a):
        self.a = a

    def sum(self):
        print('this is Parent function', self.a)
        return self.a


class ch(over):
    def sum(self):
        return self.a * 3


c = ch(5)
print(c.sum())


