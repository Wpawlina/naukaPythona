import os
import csv
import types

def exportToFileStatic(path,header,data):
    with open(path,'w') as file:
        writer=csv.writer(file,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print('Data exported to file:',path)

def exportToFileClass(cls,path):
    with open(path,'w') as file:
        writer=csv.writer(file,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','isAirBagOk','isPaintingOk','isMechanicOk','isOnSale','file'])
        for car in cls.list_of_cars:
            writer.writerow([car.brand,car.model,car.isAirBagOk,car.isPaintingOk,car.isMechanicOk,car.isOnSale,car.file if hasattr(car,'file') else ''])
    print('Class exported to file:',path)
    

def exportToFileInstance(self,path):
    with open(path,'w') as file:
        writer=csv.writer(file,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','isAirBagOk','isPaintingOk','isMechanicOk','isOnSale','file'])
        writer.writerow([self.brand,self.model,self.isAirBagOk,self.isPaintingOk,self.isMechanicOk,self.isOnSale,self.file if hasattr(self,'file') else ''] )
    print('Instance exported to file:',path)

brandOnSale='Opel'

class Car:
    number_of_cars=0
    list_of_cars=[]

    @classmethod
    def ReadFromText(cls,aText):
        cls.number_of_cars+=1
        aNewCar=cls(*aText.split(';'))
        aNewCar.file='imported from text'
        return aNewCar
    
    @staticmethod
    def ConvertKMtoKW(KM):
        return KM*0.735
    @staticmethod
    def ConvertKWtoKM(KW):
        return KW/0.735



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
    
   

   # IsOnSale=property(__GetIsOnSale,__SetIsOnSale)
    @property
    def isOnSale(self):
       return self.__isOnSale
    
    @isOnSale.setter
    def isOnSale(self,newIsOnSale):
        if self.brand==brandOnSale:
            self.__isOnSale=newIsOnSale
            print('Changing status of sale to {} for {}'.format(newIsOnSale,self.brand))
        else:
            print('Cannot change status of sale for {}'.format(self.brand))

    @isOnSale.deleter
    def isOnSale(self):
        self.__isOnSale=None

print('Static-------'*10)
exportToFileStatic(os.path.join(os.getcwd(),'srednioZaawansowany/exports/cars.csv'),['brand','model','isAirBagOk','isPaintingOk','isMechanicOk','isOnSale'],['Ferrari','Berlinetta',True,False,True,True])
Car.exportToFileStatic=exportToFileStatic
Car.exportToFileStatic(os.path.join(os.getcwd(),'srednioZaawansowany/exports/cars.csv'),['brand','model','isAirBagOk','isPaintingOk','isMechanicOk','isOnSale'],['BMW','i3',True,False,True,True])


print('-'*30)
lineOfText='Renault;Megane;True;True;True;False'
car_03=Car.ReadFromText(lineOfText)
print(car_03.__dict__)
print('-'*30)
print('Conversion:',Car.ConvertKMtoKW(120))
print('Conversion:',Car.ConvertKWtoKM(120))
lineOfText='Peugeot;308;True;False;True;True'
car_04=car_03.ReadFromText(lineOfText)
print(car_04.__dict__)
print(car_04.ConvertKMtoKW(308))
print('-'*30)

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
print('Status of cars:',car_01.isOnSale,car_02.isOnSale)
car_01.isOnSale=False
car_02.isOnSale=True
print('Status of cars:',car_01.isOnSale,car_02.isOnSale)
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

print('Class-------'*10)
Car.exportToFileClass=types.MethodType(exportToFileClass,Car)
Car.exportToFileClass(os.path.join(os.getcwd(),'srednioZaawansowany/exports/cars.csv'))

print('Instance-------'*10)
car_01.exportToFileInstance=types.MethodType(exportToFileInstance,car_01)
car_01.exportToFileInstance(os.path.join(os.getcwd(),'srednioZaawansowany/exports/car_01.csv'))
print(hasattr(car_01,'exportToFileInstance') and callable(car_01.exportToFileInstance))

print('-'*60)




def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""
 
    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)

def export_all_cakes_to_html(cls, path):
    result="<table border=1>"
    template = """
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
    """
    for cake in cls.bakeryOffer:
        result+=template.format(cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
    result+="</table>"
    with open(path, "w") as f:
        f.write(result)

class Cake:
    knownKinds=['cake','muffin','meringue','biscuit','eclair','christmas','toast','cupcake','other']
    bakeryOffer=[]  
    @classmethod
    def readFromFile(cls,fileName):
        import pickle   
        import os
        if (os.path.exists(fileName)):
            with open(fileName,'rb') as file:
                cake=pickle.load(file)   
                cls.bakeryOffer.append(cake)
                return cake
        else:
            print('File does not exist')
    @staticmethod
    def getBakeryFiles(path):
        import os
        import glob
        return glob.glob(os.path.join(path,'*.bakery'))
        



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
        Cake.bakeryOffer.append(self)
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
        
    def savaToFile(self):
        import pickle
        import os
        path=os.path.join(os.getcwd(),'srednioZaawansowany/bakery/cake_'+self.name+'.bakery')
        print('Path to save:',path)
        with open(path,'wb') as file:
            pickle.dump(self,file)
    
    def add_additives(self,additives):
        self.additives.extend(additives)

    def __getText(self):
        return self.__text
    def __setText(self,newText):
        if self.kind=='cake':
            self.__text=newText
        else:
            print('Text can be only set for cake')
    text=property(__getText,__setText)  

    def __str__(self):
        return self.kind+', '+self.name+' '+self.taste
    def __iadd__(self,newAdditives):
        res=self.additives
        if type(newAdditives)==list:
            res.extend(newAdditives)
        elif type(newAdditives)==str:
            res.append(newAdditives)
        else:
            raise Exception('Type not supported')
        return Cake(self.name,self.taste,self.kind,res,self.filling,self.__glutenFree,self.__text)
        
    
            




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
waffle.savaToFile()
vanillaCake.savaToFile()
path=os.path.join(os.getcwd(),'srednioZaawansowany/bakery/cake_Vanilla Cake.bakery')
cake_05=Cake.readFromFile(path)
print(cake_05.information())
print(Cake.getBakeryFiles(os.path.join(os.getcwd(),'srednioZaawansowany/bakery')))

for c in Cake.bakeryOffer:
    c.export_1_cake_to_html=types.MethodType(export_1_cake_to_html,c)
    c.export_1_cake_to_html(os.path.join(os.getcwd(),'srednioZaawansowany/exports/'+c.name+'.html'))
Car.export_all_cakes_to_html=types.MethodType(export_all_cakes_to_html,Cake)
Car.export_all_cakes_to_html(os.path.join(os.getcwd(),'srednioZaawansowany/exports/cakes.html'))

class noDuplicates:
    def __init__(self,func):
        self.func=func
    def __call__(self,object,list):
        newList=[i for i in list if i not in object.additives]
        self.func(object,newList)

@noDuplicates
def add_extra_additives(cake,additives):
    cake.add_additives(additives)
    
add_extra_additives(muffin,['chocolate','nuts','cherry'])
print(muffin.information())

vanillaCake+=['cherry','cream','sugar']
vanillaCake+='ice cream'
print(vanillaCake.information())



class SpecialCake(Cake):
    def __init__(self,name,taste,kind,additives,filling,glutenFree,text,occasion,shape,ornaments):
        super().__init__(name,taste,kind,additives,filling,glutenFree,text)
        self.occasion=occasion
        self.shape=shape
        self.ornaments=ornaments
    def information(self):
        res=super().information()
        res+=' Occasion: '+self.occasion+' '
        res+='Shape: '+self.shape+' '
        res+='Ornaments: '+self.ornaments+'\n'
        return res
birthdayCake=SpecialCake('Birthday Cake','chocolate','cake',['chocolate','nuts'],'cream',False,'Happy BirthDay','Birthday','round','flowers')
weddingCake=SpecialCake('Wedding Cake','vanilla','cake',['vanilla','nuts'],'cream',True,'Happy Wedding','Wedding','square','pigeons')
print(birthdayCake.information())
print(weddingCake.information())

for c in Cake.bakeryOffer:
    print(c.name)
    if isinstance(c,SpecialCake):
        print('Special cake')
    else:
        print('Normal cake')
    print('-'*30)
    


class Promo():
 
    def __init__(self, name, discount, start_date, end_date, minimal_order):
 
        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date =  end_date
        self.minimal_order = minimal_order
 
    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)


class CakePromo(Cake,Promo):
    def __init__(self,name,taste,kind,additives,filling,glutenFree,text,discount,start_date,end_date,minimal_order):
        Cake.__init__(self,name,taste,kind,additives,filling,glutenFree,text)
        Promo.__init__(self,name,discount,start_date,end_date,minimal_order)

promo_cake=CakePromo('Promo Cake','vanilla','cake',['vanilla','nuts'],'cream',True,'Happy Wedding',0.2,'2020-01-01','2020-01-15',100)
print(promo_cake.information())
print(promo_cake.full_name) 
print(CakePromo.mro())


        
   












   

        