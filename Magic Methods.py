class Demo:
    def __init__(self,radius):
        self.radius=radius
    def __add__(self,other):
        return self.radius+other.radius
    def __sub__(self,other):
        return self.radius-other.radius
    def __gt__(self,other):
        return self.radius>other.radius
    def __It__(self,other):
        return self.radius<other.radius

def main():
    d1=Demo(10)
    d2=Demo(20)
    print(d1+d2)
    print(d1-d2)
    print(d1>d2)
    print(d1<d2)
main()
