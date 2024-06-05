class Demo:
    def disp(self):
        print("Disp Started")
    def disp(self,x):
        print("Disp x Started")
    def disp(self,x,y):
        print("Disp x y Started")
    def disp(self,x,y,z):
        print("Disp x y z Started")
d=Demo()
#d.disp()#Demo.disp() missing 3 required positional arguments: 'x', 'y', and 'z
#d.disp(10)#Demo.disp() missing 2 required positional arguments: 'y' and 'z'
#d.disp(10,20)Demo.disp() missing 1 required positional argument: 'z'
d.disp(10,20,30)
