class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
class Child(Parent):
    def __init__(self):
        print("Inside Child Constructor")
c=Child()
        
class Parent1:
    def __init__(self):
        print("Inside Parent Constructor")
class Child1(Parent1):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructor")
        super().__init__()
c1=Child1()
