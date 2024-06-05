class Student:
    def __init__(self,name,rollnum,course):
        self.name=name
        self.rollnum=rollnum
        self.course=course
    def study(self):
        print("Student studying now")
    def eat(self):
        print("Student eating now")

s1=Student("Gowri",1,"Testing")
print(s1.name)
print(s1.rollnum)
print(s1.course)
s1.study()
s1.eat()
