class Addition:
    def add(self,x,y):
        print("Addition =",(x+y))
class Subtraction:
    def sub(self,x,y):
        print("Subtraction =",(x-y))
class Multiplication:
    def mul(self,x,y):
        print("Multiple =",(x*y))
class Divition:
    def div(self,x,y):
        print("Divition =",(x/y))
def calculator(ref,x,y):
    if type(ref).__name__=="Addition":
        ref.add(x,y)
    elif type(ref).__name__=="Subtraction":
        ref.sub(x,y)
    elif type(ref).__name__=="Multiplication":
        ref.mul(x,y)
    elif type(ref).__name__=="Divition":
        ref.div(x,y)
def main():
    a=Addition()
    s=Subtraction()
    m=Multiplication()
    d=Divition()
    x=int(input("Enter a 1st number"))
    y=int(input("Enter a 2st number"))
    calculator(a,x,y)
    calculator(s,x,y)
    calculator(m,x,y)
    calculator(d,x,y)
main()



















    
    
    
    
    
