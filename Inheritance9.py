class GreatGrandParent:
    def cook(self):
     print("GreatGrandParent cooks VadaPav")
class GrandParent(GreatGrandParent):
     def cook(self):
      print("GrandParent cooks LemonRice")
class Parent(GrandParent):
    def cook(self):
     print("Parent cooks Biriyani")
class Child(Parent):
    def cook(self):
     print("Child cook Veg Biriyani")
     super(Child,self).cook()
     super(Parent,self).cook()
     super(GrandParent,self).cook()
c=Child()
c.cook()
