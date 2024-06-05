
a=int(input("Enter a first number : " ))
b=int(input("Enter a second number : " ))
c=(a+b)/2
print("The average of" ,a ,"and", b ,"is :" ,c)

print("if else condition example")

a=int(input("Enter a number : "))
if a%5==0:
    print("The entered number:" ,a,"is divisible by 5")
else:
    print("The entered number",a,"is not divisible by 5")

print("if elif condition example")

course=input("Enter a course name: ")
if course=="MCP1":
    print("Fullstack Development Course")
elif course=="MCP2":
        print("Software Tesing Course")
else :
    print("invalid course")

print("match condition example")

a=int(input("Enter a first number : "))
b=int(input("Enter a second number : "))
c=int(input ("Enter your choice : "))
match c:
      case 1:print(a+b)
      case 2:print(a-b)
      case 3:print(a*b)
      case 4:print(a/b)
      case _:print("Invalid Choice")
                















      



    

    
