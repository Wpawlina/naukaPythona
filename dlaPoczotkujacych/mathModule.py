import math
math_ls = dir(math) 
print(math_ls)

import random

print(random.randint(1,100)) #1<=N<=100

print(random.choice([1,2,7,88,232,2656,11111,564141]))

print(random.choice(range(1,100)),random.randrange(1,100))
list=['John','Ann','Peter','Susan','Emilu','Greg','Chris']
random.shuffle(list)
print(list)
print(random.random())

res=random.randint(1,100)
attampts=1
curA=random.randint(1,100)
while curA!=res:
    curA=random.randint(1,100)
    attampts+=1
print(curA,attampts)
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

Groups=[[]for _ in range(len(countries)//4 +1 )]
total=0
curIndex=0
random.shuffle(countries)
while total<len(countries):
    Groups[curIndex]=countries[total:total+4]
    total+=4
    curIndex+=1
print(Groups)

numbers=[1]
line=''
for num in numbers:
    line+="%3d " % (num)
width=60
print(line.center(width))
levels=10
for i in range(levels-1):
    newNumbers=[1]
    for i in range(len(numbers)-1):
        newNumbers.append(numbers[i]+numbers[i+1])
    newNumbers.append(1)
    numbers=newNumbers
    line=''
    for num in numbers:
        line+="%3d " % (num)
    print(line.center(width))






    
    
