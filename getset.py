class encap():
    def __init__(self):
        self.__a = 0
        self.__b = 0

    def setAge(self, a, b):
        self.__a = a
        self.__b = b

    def getAge(self):
        return self.__a, self.__b


en = encap()
en.setAge(40, 50)
print(en.getAge())
