class A:
    def __init__(self, a, b):
        print("inside constructor")
        self.a = a
        self.b = b

    def sum(self, l):
        c = self.a + self.b + l
        return c


class B(A):
    pass


bo = B(10, 5)
print(bo.sum(3))


class st():
    @staticmethod
    def display():
        print("inside static method")


st.display()

class F(A):
    def sum(self,b):
        print(b)
    def over(self,p,i):
        print(i)
    
f=F(2,3)
