class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def barks(self):
        print("Dog barks")
    def eat(self):
        print("Dog eats Biriyani")
def main():
    d1=Dog("Tiger","Black")
    d1.barks()
    d1.eat()
    print(d1.name," ",d1.color)
main()
