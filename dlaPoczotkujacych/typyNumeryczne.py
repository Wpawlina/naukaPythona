import sys
print(sys.maxsize)
veryBigValue=9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
veryBigValue+=1
print(veryBigValue)
print(type(veryBigValue))
print(5/3)
print(5//3)
print(5%3)
inf='inf'
inf=float(inf)
print(inf>veryBigValue)
inf=-float(inf)
print(inf>veryBigValue)
name='Wojciech'
age=20
daysInYear=365
message='{:s} is {:d} years old, so is about {:d} days old'
print(message.format(name,age,age*daysInYear))
name='Jan'
age=45
print(message.format(name,age,age*daysInYear))
message='{:d} divided by {:d} is {:d} and the rest is {:d}'
num1=1234567890
num2=12345
print(message.format(num1,num2,num1//num2,num1%num2))

val1=126
val2='126'
val3=126.0
val4='126.0'
print(val1,type(val1))
print(val2,type(val2))
print(val3,type(val3))
print(val4,type(val4))
print(val1+val3,type(val1+val3))
print(val2+val4,type(val2+val4))
print(7-1*0+3+3)
print(4**5/2**3)



