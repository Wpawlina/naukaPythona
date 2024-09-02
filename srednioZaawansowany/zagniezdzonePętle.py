listA=list(range(6))
listB=list(range(6)) 

print(listA,listB)

product=[]
for a in listA:
    for b in listB:
        product.append((a,b))
print(product)
print('===============================')

product2=[(a,b) for a in listA for b in listB]

print(product2)
print('===============================')

prioduct3=[(a,b) for a in listA for b in listB if a%2==1 and b%2==0]

print(prioduct3)
print('===============================')

product4={a:b for a in listA if a%2==1 for b in listB if a%2==1 and b%2==0}
print(product4)
print('===============================')


ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections=[(a,b) for a in ports for b in ports if a<b]
print(connections,len(connections))

gen=((a,b) for a in ports for b in ports if a<b)
print(gen)

print(next(gen))
print(next(gen))
print('===============================')

for f in gen:
    print(f)    

print('===============================')
cnt=0
gen=((a,b) for a in ports for b in ports if a<b)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break
    cnt+=1
print('Number of connections:',cnt)