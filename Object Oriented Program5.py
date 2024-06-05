class Demo:
    a=10
    b=20
    def __init__(self,x,y):
       self.x=x
       self.y=x
    def fun(self):
       print("Python is Fun")
d=Demo(100,200)
d.fun()
print(d.x)
print(d.y)
print(d.a)
print(d.b)
#print(Demo.x)error-->Instance varibles cannot be accessed using class name
#print(Demo.y)
print(Demo.a)
print(Demo.b)
