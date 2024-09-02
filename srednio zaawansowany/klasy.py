brandOnSale='Opel'

class Car:
    number_of_cars=0
    list_of_cars=[]
    def __init__(self,brand,model,isAirBagOk,isPaintingOk,isMechanicOk,isOnSale=False):
        Car.number_of_cars+=1
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.__isOnSale = isOnSale
        Car.list_of_cars.append(self)
    
    def isDamaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMechanicOk)
    def GetInfo(self):
        print('{} {}'.format(self.brand,self.model).upper())
        print('Air Bag  - ok -   {}'.format(self.isAirBagOk))
        print('Painting - ok -   {}'.format(self.isPaintingOk))
        print('Mechanic - ok -   {}'.format(self.isMechanicOk))
        print('IS ON SALE        {}'.format(self.__isOnSale))
        print('-'*30)
    def __GetIsOnSale(self):
        return self.__isOnSale
    def __SetIsOnSale(self,newIsOnSale):
        if self.brand==brandOnSale:
            self.__isOnSale=newIsOnSale
            print('Changing status of sale to {} for {}'.format(newIsOnSale,self.brand))
        else:
            print('Cannot change status of sale for {}'.format(self.brand))
    IsOnSale=property(__GetIsOnSale,__SetIsOnSale)

print('Class level variables before creating instances:',Car.number_of_cars,Car.list_of_cars)
car_01 = Car('Seat','Ibiza',True,True,True,False)
car_02=Car('Opel','Corsa',True,False,True,True)
print('Class level variables after creating instances:',Car.number_of_cars,Car.list_of_cars)
car_01.year=2005
del car_01.year
setattr(car_01,'year',2006)
print(hasattr(car_01,'year'))
delattr(car_01,'year')

#print('Status of cars:',car_01.GetIsOnSale(),car_02.GetIsOnSale())
#car_01.SetIsOnSale(True)
#car_02.SetIsOnSale(False)
car_01.IsOnSale=False
car_02.IsOnSale=True
print('-'*30)

print(car_01.brand,car_01.model,car_01.isAirBagOk,car_01.isPaintingOk,car_01.isMechanicOk)
print(car_02.brand,car_02.model,car_02.isAirBagOk,car_02.isPaintingOk,car_02.isMechanicOk)

print(car_01.isDamaged())
print(car_02.isDamaged())
print('-'*30)
print(car_01.GetInfo())
print(car_02.GetInfo())
print('-'*30)
print('Id of class:',id(Car),type(Car))
print('Id of object:',id(car_01),type(car_01),id(car_02),type(car_02))
print('check if object belongs to class:',isinstance(car_01,Car))
print('check if object belongs to class with __class__:',car_01.__class__)
print('list of instance attributes :',vars(car_01))
print('list of class attributes :',vars(Car))
print('list of class attributes with values:',dir(Car))
print('list of class attributes with values:',dir(Car))
print('Value taken from instance',car_01.number_of_cars,'Value taken from class:',Car.number_of_cars)
print('-'*60)

class Cake:
    knownKinds=['cake','muffin','meringue','biscuit','eclair','christmas','toast','cupcake','other']
    def __init__(self,name,taste,kind,additives,filling,glutenFree=False,text=''):
        self.name=name
        self.taste=taste
        if kind in Cake.knownKinds:
            self.kind=kind
        else:
            self.kind='other'
        self.additives=additives
        self.filling=filling
        self.__glutenFree=glutenFree
        if self.kind=='cake':
            self.__text=text
        else:
            self.__text=''
    def information(self):
        result=self.name+' - '+self.kind+' main tatse: '+self.taste+ ' with additives of \n ['
        for a in self.additives:
            result+=a+','
        result=result[:-1]
        result+='] and filling of '+self.filling +'\n Gluten free: '+str(self.__glutenFree)+'\n Text: '+self.__text
        return result
    def setFilling(self,filling):
        self.filling=filling
    def addAdditives(self,additives):
        self.additives.extend(additives)
    def __getText(self):
        return self.__text
    def __setText(self,newText):
        if self.kind=='cake':
            self.__text=newText
        else:
            print('Text can be only set for cake')
    text=property(__getText,__setText)  




muffin=Cake('Muffin','chocolate','cupcake',['chocolate','nuts'],'')
vanillaCake=Cake('Vanilla Cake','vanilla','cake',['chocolate','nuts'],'Cream',True)
meringue=Cake('Super sweet Meringue','meringue','meringue',[],'')
waffle=Cake('Cocoa Waffle','waffle','cocoa',[],'cocoa')
waffle.text='Text for waffle'
vanillaCake.text='Text for cake'
cakes=[muffin,vanillaCake,meringue,waffle]
muffin.setFilling('chocolate')
vanillaCake.addAdditives(['ice cream','raspberry'])
for c in cakes:
    print(c.information())



   

        