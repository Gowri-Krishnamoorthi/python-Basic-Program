tuple=(10,20,30,40,50)
print(tuple)
print(type(tuple))#homogenius

tup1=(10,20,30,40,50,20.5,"K",8+5j)
print(tup1)
print(type(tup1))#hetrogenius

tuple3=(10,20,30,40,50,50,20)
print(tuple3)
print(type(tuple3))#duplicates

'''tuple.append(100)#error
tuple.extend(400,400)#error

tuple.insert()//error
tuple.remove(20)//error'''#tuples are immutable in nature.

del tuple
print(tuple)
