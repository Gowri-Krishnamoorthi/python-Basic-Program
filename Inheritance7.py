class Parent1:
    def bekind(self):
        print("Bekind in Parent1")
    def cook(self):
        print("Cook in Parent1")
class Child(Parent1):
    def cook(self):
        print("Cook in Child")
    def play(self):
        print("Play in child")
c=Child()
c.bekind()
c.cook()
c.play()
