
print("Callable class instance")

class MemoryClass:
    def __init__(self,list):
        self.list_of_items=list
    def __call__(self, item):
        self.list_of_items.append(item)
       

mem=MemoryClass([1,2,3,4,5])   
print("Class: ", callable(MemoryClass), "Instance: ",callable(mem))
print(mem.list_of_items)
mem.list_of_items.append(6)
mem(7)





class NoDuplicates:
    def __init__(self):
        self.items = []
    def __call__(self, new_item):
        if new_item not in self.items:
            self.items.append(new_item)
myNoDupList = NoDuplicates()    
myNoDupList('keyboard')
myNoDupList('mouse')
myNoDupList('keyboard')
myNoDupList('monitor')  
print(myNoDupList.items)

print('='*60)
print('Klasa jako dekorator')

class MemoryClass:
    listOfAlreadyTakenItems=[]

    def __init__(self,fun):
        print('MemoryClass init')
        self.fun=fun
    def __call__(self, list):
        print('MemoryClass call')
        itemsNotSelected=[i for i in list if i not in self.listOfAlreadyTakenItems]
        item=self.fun(itemsNotSelected)
        MemoryClass.listOfAlreadyTakenItems.append(item)
        return item
        
       
            
        

import random

cars=['Opel','Toyota','Ford','BMW','Mercedes','Audi','VW','Fiat','Renault','Peugeot']

@MemoryClass
def selectTodayPromotion(cars):
    return random.choice(cars)

@MemoryClass
def SelectTodayShow(cars):
    return random.choice(cars)

@MemoryClass
def SelectFreeGift(cars):
    return random.choice(cars)

print('Promotion :',selectTodayPromotion(cars))
print('Show :',SelectTodayShow(cars))
print('Gift :',SelectFreeGift(cars))

print('='*60)

class Car:
    def __init__(self,brand,model,price,isAirBagOk,isPaintingOk,isMechanicOk,accessries=[]):
        self.brand=brand
        self.model=model
        self.price=price
        self.isAirBagOk=isAirBagOk
        self.isPaintingOk=isPaintingOk
        self.isMechanicOk=isMechanicOk
        self.accessories=accessries
    def __iadd__(self,newAccessories):
        accesories=self.accessories
        if type(newAccessories)==list:    
            accesories.extend(newAccessories)
        elif type(newAccessories)==str:
            accesories.append(newAccessories)
        else:
            raise Exception('{} Type not supported'.format(type(newAccessories)))
        return Car(self.brand,self.model,self.price,self.isAirBagOk,self.isPaintingOk,self.isMechanicOk,accesories)
    
    def __add__(self,other):
        if type(other) is Car:
            return [self,other]
        else:
            raise Exception('{} Type not supported'.format(type(other)))
    def __str__(self):
        return '{} {}'.format(self.brand,self.model)

car_01=Car('Seat','Ibiza',price=20000,isAirBagOk=True,isPaintingOk=True,isMechanicOk=True,accessries=['alarm','winter tires'])
car_01+=['navigation','roof rack']
car_01+='sport suspension'
#car_01+=1
print(car_01.__dict__)

car_02=Car('Opel','Corsa',price=21000,isAirBagOk=True,isPaintingOk=False,isMechanicOk=True,accessries=['alarm','summer tires','heated seats'])
carPack=car_01+car_02
print(carPack)
print(carPack[0])




