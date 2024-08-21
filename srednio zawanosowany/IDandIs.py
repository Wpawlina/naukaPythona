myvar='Hello World'
myvar2=myvar
print(myvar,myvar2)
print(type(myvar),type(myvar2)) 
print('Is value the same ?',myvar == myvar2)
print('Are the variables the same ?',myvar is myvar2)
print(id(myvar),id(myvar2))
print('===============================')

myvar2=myvar2+'!'
print(myvar,myvar2)
print(type(myvar),type(myvar2)) 
print('Is value the same ?',myvar == myvar2)
print('Are the variables the same ?',myvar is myvar2)
print(id(myvar),id(myvar2))
print('===============================')

myvar2=myvar2[:-1]
print(myvar,myvar2)
print(type(myvar),type(myvar2)) 
print('Is value the same ?',myvar == myvar2)
print('Are the variables the same ?',myvar is myvar2)
print(id(myvar),id(myvar2))
print('===============================')

a=10
b=10
c=10
print(a,id(a),b,id(b),c,id(c))
a=20
print(a,id(a),b,id(b),c,id(c))
print('===============================')

a=[1,2,3]
b=a
c=a
print(a,id(a),b,id(b),c,id(c))
a.append(4)
print(a,id(a),b,id(b),c,id(c))
print('===============================')

x=10
y=10
print(x,id(x),y,id(y))

y-=1
y+=1
print(x,id(x),y,id(y))


y+=1234567890
y-=1234567890
print(x,id(x),y,id(y))



