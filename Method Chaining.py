class Parent:
    def cook(self):
        print("Parent cooks biriyani")
    def fun(self):
        print("Inside Parent")
class Child(Parent):
    def cook(self):
        super().cook()
        print("Child cooks Veg biriyani")
        super().cook()
        super().fun()
c=Child()
c.cook()
