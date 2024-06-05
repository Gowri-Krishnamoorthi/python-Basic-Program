list=[10,20,30,40,50,60,70,80]
print(list)
print(type(list))

list1=[10,20.5,True,"K",10+5j]
print(list1)
print(type(list))#allow homogenius and hetrogenius data

list2=[10,10,20,20,30]
print(list2)
print(type(list2))#allows duplicate values

print(list[3])#40

for i in list:
    print(i,end=' ')#iteratable objects , does contain the index position
    
    
list.append(100)
print(list)

list.extend([200])
print(list)

'''list.append(200,300)
print(list)'''# we can append only one element at the time.

list.extend([11,22,33])
print(list)

list.append([200,300])#we can append one list at the time,but it has how many variables it not a prm
print(list)

list.insert(3,0.00)
print(list)

'''list.push(10)
print(list)'''#error list does not having the attribute
print()
print()
print()


list.remove(40)
print(list)

list.pop()
print(list)#removing the last element

list.pop(1)
print(list)#specified index

del list[1]
print(list)

list.clear()
print(list)#[]

del list#deletes the datastruture from the memory

print(list)#error

























