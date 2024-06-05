class Demo:
    def __init__(self):
        print("Inside __init__()")
    def __init__(self,a):
        print("Inside __init__(a)")
    def __init__(self,a,b):
        print("Inside __init__(a,b)")
    def __init__(self,a,b,c):
        print("Inside __init__(a,b,c)")
#d=Demo()Demo.__init__() missing 3 required positional arguments: 'a', 'b', and 'c'
#d=Demo(10)Demo.__init__() missing 2 required positional arguments: 'b' and 'c'
#d=Demo(10,20)Demo.__init__() missing 1 required positional argument: 'c'
d=Demo(10,20,30)#Inside __init__(a,b,c)

