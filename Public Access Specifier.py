#public access specifier

class Demo:
    def __init__(self):
        self.x=10
        self.y=20
class Test:
    def display(self):
        d=Demo()
        print("Inside the Test Class")
        print(d.x)#Accessing public varible inside another class
        print(d.y)
d1=Demo()
print(d1.x)#Accessing public variable outside the class
print(d1.y)
t=Test()
t.display()
