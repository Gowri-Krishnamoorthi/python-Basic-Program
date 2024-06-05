#Private

class Demo:
    def __init__(self):
        self.__x=10
        self.__y=20
d=Demo()
#print(d.__x)#Error:Accessed outside the class
#print(d.__y)
print(d._Demo__x)#10
print(d._Demo__y)#20
