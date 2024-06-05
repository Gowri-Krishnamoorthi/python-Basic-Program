s={10,20,30,40,50}
print(s)
print(type(s))#unordered collection of data,homogenius

s1={10,20.0,30.5,True,"G",3+4j}
print(s1)
print(type(s1))#hetro genius

s2={10,20,30,40,50,50,40}
print(s2)
print(type(s2))#duplicated not allowed

'''print(s[3])'''#not based on index
for i in s1:
    print(i,end=' ')

print()
s.add(100)#one element
print(s)

s.update({11,22,33})
print(s)

s.pop()
print(s)#first element

s.pop()
print(s)

s.remove(11)
print(s)

s.clear()
print(s)

del s
print(s)















