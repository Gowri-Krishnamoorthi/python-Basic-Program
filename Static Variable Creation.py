class Student:
    Institude="Kodnest"#static variable
    def __init__(self):
        self.name="Raj"
        Student.course="MCP1"#static variable
    @staticmethod
    def play():
        print("Inside Static method")
        Student.play="Football"
    @classmethod
    def class_method(cls):
        print("Inside class method")
        Student.need="Job"
        cls.eat="Food"
print(Student.Institude)
s=Student()
print(Student.course)
Student.play()
Student.class_method()
print(Student.play)
print(Student.need)
print(Student.eat)


        
