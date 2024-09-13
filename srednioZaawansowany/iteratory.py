print('Iteratory')

import datetime as dt
import sys

start=dt.datetime.now()
print('Start:',start)

dates=[dt.date(2000,1,1)+dt.timedelta(days=i) for i in range(2500000)]
print('sieze of dates is {}'.format(sys.getsizeof(dates)))
for d in dates:
    pass

class MillionDays:
    def __init__(self,year,month,day,maxdays):
        self.date=dt.date(year,month,day)
        self.maxdays=maxdays    

    def __next__(self):
        if self.maxdays<=0:
            raise StopIteration()
        ret=self.date
        self.date+=dt.timedelta(days=1)
        self.maxdays-=1
        return ret
    
    def __iter__(self):
        return self



md=MillionDays(2000,1,1,2500000)

for i in range(2500000):
    next(md)
print('sieze of md is {}'.format(sys.getsizeof(md)))    

#for d in iter(md):
 #   pass

for d in md:
    pass

stop=dt.datetime.now()
print('Stop:',stop)

print('='*60)
print('GetItem')


class MillionDays:
    def __init__(self,year,month,day,maxdays):
        self.date=dt.date(year,month,day)
        self.maxdays=maxdays    
    
    def __getitem__(self, item):
        if item>=self.maxdays:
            raise IndexError
        return self.date+dt.timedelta(days=item)
    
md=MillionDays(2000,1,1,10)
print(md[0],md[1],md[4],md[9])

it=iter(md)
print(next(it))
print(next(it))

for d in iter(md):
    print(d)

print('='*60)
print('iteroy dla typów systemowych')

aTuple=(1,2,3,4,5)

it=iter(aTuple)
print(next(it))
print(next(it))
print(next(it))

aSet={1,2,(3,4),'another element',3,4} 
it=iter(aSet)
print(next(it))

print('='*60)   
import time
 
products = ["Product {}".format(i) for i in range(1, 500)]

 
promotions = ["Promotion {}".format(i) for i in range(1, 50)]

 
customers = ['Customer {}'.format(i) for i in range(1, 500)]


 
class Combination:
    def __init__(self,products,promotions,customers):
        self.products=products
        self.promotions=promotions
        self.customers=customers
        self.currentProduct=0
        self.currentPromotion=0
        self.currentCustomer=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.currentProduct>=len(self.products):
            self.currentProduct=0
            self.currentPromotion+=1
        if self.currentPromotion>=len(self.promotions):
            self.currentPromotion=0
            self.currentCustomer+=1
        if self.currentCustomer>=len(self.customers):
            raise StopIteration()
        item='{} - {} - {}'.format(self.products[self.currentProduct],self.promotions[self.currentPromotion],self.customers[self.currentCustomer])
        self.currentProduct+=1
        return item
    
combination=Combination(products,promotions,customers)
for c in combination:
    pass
print('size of combination is {}'.format(sys.getsizeof(combination)))



class Combination:
    def __init__(self,products,promotions,customers):
        self.products=products
        self.promotions=promotions
        self.customers=customers
      
    
    def __getitem__(self, item):
        posCustomer=item//(len(self.promotions)*len(self.products))
        item=item%(len(self.promotions)*len(self.products))
        posPromotion=item//len(self.products)
        item=item%len(self.products)
        posProduct=item

        return '{} - {} - {}'.format(self.products[posProduct],self.promotions[posPromotion],self.customers[posCustomer])
   


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]
 
combinations = Combination(products, promotions, customers)

iterCombinations=iter(combinations)
print(next(iterCombinations))
print(next(iterCombinations))



for i in range(30):
    print(combinations[i])



   

import csv
import os




with open('srednioZaawansowany/test2.txt', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #for row in csvreader:
        #print('|'.join(row))
    for row in csvreader:
        try:
            print(next(csvreader))
        except StopIteration:
            break
