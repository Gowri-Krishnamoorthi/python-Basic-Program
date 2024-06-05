class Parent1:
    def fun(self):
        print("fun() in parent1")
    def fun1(self):
        print("fun1() in parent1")
class Parent2(Parent1):
    def fun2(self):
        print("fun2() in parent2")
class Child(Parent2):
    pass
c=Child()
c.fun()
c.fun1()
c.fun2()
