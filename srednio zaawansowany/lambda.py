def double(x):
    return x * 2    

x=10
print(double(x))

f=lambda x: x*2
x=10
print(f(x))

def power(x,y):
    return x**y

x=5
y=3
print(power(x,y))   

f=lambda x,y: x**y  
print(f(x,y))

list_number=[1,2,3,4,11,15,20,21]

def isOdd(x):
    return x%2!=0

filter_list=list(filter(isOdd,list_number))
print(filter_list)

filter_list=list(filter(lambda x: x%2!=0,list_number))


def generate_multiply_function(n):
    return lambda x: x*n


mul2=generate_multiply_function(2)  
mul3=generate_multiply_function(3)


text_list=['x','xxx','xxxxx','xxxxxxx','']
f=lambda x: len(x)  

print(f('xxxxx'))

length_list=list(map(f,text_list))

length_list=list(map(lambda x: len(x),text_list))
