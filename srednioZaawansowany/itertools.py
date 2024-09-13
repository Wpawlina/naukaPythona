import itertools


mylist=['a','b','c','d']
print('Kombinacje')
for combination in itertools.combinations(mylist,3):
    print(combination)
print('='*60)
print('Permutacje/Wariacje bez powtórzeń')
for perm in itertools.permutations(mylist,3):
    print(perm)
print('='*60)
print('Kombinacje z powtórzeniami')
for combination in itertools.combinations_with_replacement(mylist,3):
    print(combination)
print('='*60)
print('Produkt kartezjański/wariacje z powtórzeniami')
for product in itertools.product(mylist,repeat=3):
    print(product)
print('='*60)
money=[20,20,20,20,10,10,10,10,5,5,1,1,1,1,1]
result=[]

for i in range(1,101):
    for combination in itertools.combinations(money,i):
        if sum(combination)==100:
            result.append(combination)
result=set(result)

for r in result:    
    print(r)
print('='*60)
print('Group by')
filepath='srednioZaawansowany/data.txt'
data=[]

with open(filepath) as file:
    for line in file:
        if ':' in line:
            type,action=line.rstrip('\n').split(':',1)
            record={'type':type,'action':action}
            data.append(record)
data=sorted(data,key=lambda x:x['type'])
for key,elements in itertools.groupby(data,key=lambda x:x['type']):
    print('The key is:',key,'The number of elements:',len(list(elements)))


import os

def scanTree(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scanTree(entry.path)
        else:
            yield entry
dir='srednioZaawansowany'
tree=scanTree(dir)
listing=[]
for i,entry in enumerate(tree):
    print(i,entry.path,entry.is_dir(),entry.is_file())
    listing.append(entry)
listing=sorted(listing,key=lambda x:x.is_dir())
for is_dir,elements in itertools.groupby(listing,key=lambda x:x.is_dir()):
    print('Is dir:',is_dir,'Number of elements:',len(list(elements)))
print('='*60)
print('Pozostałe funkceje itertools')
import operator
print('Accumulate')
data=[1,2,3,4,5,6,7,8,9,10]
result=itertools.accumulate(data,operator.mul)
print(list(result))
print('='*30)
print('count')
for i in itertools.count(10,2):
    if i>20:
        break
    print(i)
print('='*30)

print('cycle')
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i,month in enumerate(itertools.cycle(months)):
    print(month)
    if i>15:
        break
print('='*30)

print('chain')
color_basic=['red','blue','yellow']
color_mix=['green','yellow','black']    
result=itertools.chain(color_basic,color_mix)
print(list(result))
print('='*30)

print('compress')
cars=['Opel','Toyota','Ford','BMW','Mercedes','Audi','VW','Fiat','Renault','Peugeot']
selector=[True,False,True,False,True,False,True,False,True,False]
print(list(itertools.compress(cars,selector)))
print('='*30)

print('dropwhile')
data=[1,2,3,4,5,6,1,7,8,9,10]
result=itertools.dropwhile(lambda x:x<5,data)
print(list(result))
print('='*30)

print('filterfalse')
data=[1,2,3,4,5,6,7,1,8,9,10]
result=itertools.filterfalse(lambda x:x<5,data)
print(list(result))
print('='*30)

print('islice')
data=[1,2,3,4,5,6,7,8,9,10]
result=itertools.islice(data,3,7)
print(list(result))
print('='*30)
print('product')

spades=['Hearts','Diamonds','Clubs','Spades']  
figures=['Ace','King','Queen','Jack','10','9','8','7','6','5','4','3','2']
result=itertools.product(spades,figures)
print(list(result))
print('='*30)
print('repeat')

for i in itertools.repeat('Python',5):
    print(i)
print('='*30)

print('starmap')
data=[(2,3),(4,5),(6,7),(8,9)]
result=itertools.starmap(operator.add,data)
print(list(result)) 
print('='*30)

print('takewhile')
data=[1,2,3,4,5,6,1,7,8,9,10,1]
result=itertools.takewhile(lambda x:x<5,data)
print(list(result))

print('='*30)
print('tee')
cars=['Opel','Toyota','Ford','BMW']
iter1,iter2=itertools.tee(cars)
for each in iter1:
    print(each)
for each in iter2:
    print(each)
print('='*30)

print('zip_longest')
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
plans=['busy','busy','free','free','busy','busy','free']
result=itertools.zip_longest(months,plans,fillvalue='unknown')
print(list(result))