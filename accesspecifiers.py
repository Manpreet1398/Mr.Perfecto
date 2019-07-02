class access:
    a = 10
    _b = 20

    def _sum(self):
        print("invalid method")


p = access()
print(p._b)
p._sum()


class pvt:
    a = 10
    _b = 20
    __c = 30

    def display(self):
        print("invalid public method")

    def _dis(self):
        print("invalid protected method")

    def __distance(self):
        print("invalid pvt method")


p = pvt()
#print(p.__c)  # attribute error because private
print(p._b)
p.__distance()



