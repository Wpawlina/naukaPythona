varx=10
password='My password'

source='varx + 2'
result=eval(source)

print(result)



source='password'
result=eval(source)
print(result)

#globals=globals().copy()
#del globals['password'] 

result=eval(source,{'password':'*******'})
print(result)

globals={}

source='__import__("os").getcwd()'
result=eval(source,globals)
print(result)

import math


val=0
argument_list=[]
while val<10:
    argument_list.append(val)
    val+=0.1
    val=math.ceil(val*10)/10
source=input('Enter the function with x argument: ')

for x in argument_list:
    print('x=',x,'result=',eval(source))



