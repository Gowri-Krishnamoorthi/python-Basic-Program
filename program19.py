d={1:"one",2:"Two",3:"Three"}
print(d)
print(type(d))

d1={1:"one",9+5j:"Two","Raj":"Three"}
print(d1)
print(type(d1))

d2={1:"one",1:"Two",2:"Raj",1:"Python"}
print(d2)
print(type(d2))#duplicate key -->last value

d3={1:"Python",2:"Python",3:"Python"}
print(d3)
print(type(d3))

print(d[3])#key value

for i in d:
    print(i,end=' ')#key
print()
for i in d:
    print(d[i],end=' ')#values
print()
for i in d:
    print(i,":",d[i])
print()
for i in d.keys():
    print(i,end=' ')
print()
for i in d.values():
    print(i,end=' ')
print()
for i in d.items():
    print(i)
print()

d.update({"name":"Raj","age":24})
print(d)

del d[3]
print(d)#key deleted

'''d.pop()#error'''

d.pop(2)
print(d)#key deleted

d.popitem()
print(d)#last item deleted

d.clear()
print(d)

del d
print(d)






































    
















