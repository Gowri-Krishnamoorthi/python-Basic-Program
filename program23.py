#count of vowels in the given string
a=input("Enter a String:")
a1=a.upper()
print(a1)
count=0
for i in a1:
    if (i=='A' or i=='E'or i=='O'or i=='I'or i=='U'):
        count+=1
print("The Entered Vowel Count Is : ",count)

s=input("Enter a String : ")
s1=s.upper()
c=0
v=0
sp=0
for i in s1:
    if(i>='A' and i<='Z'):
        if(i=='A' or i=='E'or i=='I'or i=='O'or i=='U'):
            v+=1
        else:
            c+=1
    else:
        sp+=1
print("Number of Vowels",v)
print("Number of Consonents",c)
print("Number of Special Character",sp)





    


