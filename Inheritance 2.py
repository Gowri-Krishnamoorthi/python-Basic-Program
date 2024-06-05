class Parent1:
    def __init__(self):
        self.x=10
        self.y=200
    def fun(self):
        print("Inside the Parent1 fun")
    def fun1(self):
        print("Inside the Parent1 fun1")
class Parent2:
    def __init__(self):
        self.x=10
        self.y=20
    def fun(self):
        print("Inside the Parent2 fun")
class Child(Parent2):
    pass
c=Child()
print(c.x)
print(c.y)
c.fun()
