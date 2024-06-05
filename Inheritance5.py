class Parent1:
    def __init__(self):
        self.x=10
    def fun(self):
        print("Inside Parent1")
class Parent2:
    def __init(self):
        self.x=200
    def fun1(self):
        print("Inside Parent2")
class Child(Parent2,Parent1):
    pass
c=Child()
print(c.x)
c.fun()
c.fun1()
print(Child.__mro__)
