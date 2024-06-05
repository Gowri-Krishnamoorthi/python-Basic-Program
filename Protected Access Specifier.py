#Protected access specifier

class Demo:
    def __init__(self):
        self._x=10
        self._y=20
class Test(Demo):
    def display(self):
        d=Demo()
        print("Inside the Test Class")
        print(d._x)#Accessing public varible inside another class
        print(d._y)
d1=Demo()
print(d1._x)#Accessing protected variable outside the class
print(d1._y)
t=Test()
t.display()
