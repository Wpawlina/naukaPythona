brandOnSale = 'Opel'
class Car:
    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        print('Car init',self.__class__.__name__)
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOK))
        print("Painting - ok - {}".format(self.isPaintingOK))
        print("Mechanic - ok - {}".format(self.isMechanicOK))
        print("IS ON SALE - {}".format(self.__isOnSale))
        print('---------------------------')

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available in sale/promo')

class Truck(Car):
    def __init__(self, brand, model,  isAirBagOK, isPaintingOK, isMechanicOK, isOnSale,capacity):
        super().__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale)
        print('Truck init',self.__class__.__name__)
        #Car.__init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale) To samo
        self.capacity = capacity

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOK))
        print("Painting - ok - {}".format(self.isPaintingOK))
        print("Mechanic - ok - {}".format(self.isMechanicOK))
        print("IS ON SALE - {}".format(self.__isOnSale))
        print('Capacity: {}'.format(self.capacity))
        print('---------------------------')


truck_01 = Truck('Ford', 'Transit', True, True, True, False, 1600)
truck_02= Truck('Reanult', 'Traffic', True, False, True, True, 1200)
print(truck_01.__dict__)
print(truck_02.__dict__)
truck_01.GetInfo()



              
