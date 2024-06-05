class Parent:
    def __init__(self):
        self.x=10
        self.y=20
    def fun(self):
        print("Inside Parent Class")
class Child(Parent):
    pass
c=Child()
print(c.x)
print(c.y)
c.fun()
