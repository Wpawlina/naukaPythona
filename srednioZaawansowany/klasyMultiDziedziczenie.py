
        


class Car:
    def __init__(self,brand,model,price):
        print('Car init start')
        self.brand=brand
        self.model=model
        self.price=price
        self.name=brand+' '+model
        print('Car init stop')
    def GetInfo(self):
        print('Car GetInfo start')
        super().GetInfo()
        print('Name:', self.brand +' '+ self.model,' Price:',self.price)
        print('Car GetInfo stop')



class SpecialList:
    def __init__(self,firstName,lastName,brand):
        print('SpecialList init start')
        self.firstName=firstName
        self.lastName=lastName
        self.name=firstName+' '+lastName
        self.brand=brand
        print('SpecialList init stop' )
    def GetInfo(self):
        print('SpecialList GetInfo start')
        print('Name:',self.firstName + ' ' + self.lastName ,' Brand:',self.brand)
        print('SpecialList GetInfo stop')

class CarSpecialist(Car,SpecialList):
    def __init__(self,brand,model,price,firstName,lastName):
        '''CarSpecialist init'''
        print('CarSpecialist init start')
        Car.__init__(self,brand,model,price)
        SpecialList.__init__(self,firstName,lastName,brand.upper())
        print('CarSpecialist init stop')
    def GetInfo(self):
        print('CarSpecialist GetInfo start')
        super().GetInfo()
        print('CarSpecialist GetInfo stop')

tom=CarSpecialist('Ford','Focus',20000,'Tom','Smith')
print(vars(tom))
tom.GetInfo()
       
print(CarSpecialist.__mro__)
