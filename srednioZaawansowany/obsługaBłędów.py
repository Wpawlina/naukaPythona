print('Exceptions handling')

clients={
    "INFO":0.5,
    "DATA":0.2,
    "SOFT":0.2,
    "INTER":0.1,
    "OMEGA":0.0
}

myClient=input("Podaj nazwę klienta: ").upper()
totalCos=7200
try:
    ratio=float(input("Podaj wprocentowaniu dla klienta {}: ".format(myClient)))/100
    print("The default ratio for {} is {}, a new one is {}".format(myClient,clients[myClient],ratio))
    print("The cost for {} is {}".format(myClient,ratio*totalCos))
    print("The new ratio in comparsion to old ratio is {}".format(clients[myClient]/ratio))
except KeyError as e: 
    print("The client {} is not on the list, the error is {}".format(myClient,e))
except (ValueError,ZeroDivisionError) as e:
    print("The new ratio must be a number greater than 0 , the error is {}".format(e))
#except ZeroDivisionError as e:
 #   print("The new ratio can't be 0, the error is {}".format(e))
except Exception as e:
    print("The error is: ",e)
else:
    print('Success')
finally:
    print("="*60)
    
print("Raising Exceptions")

def ProccessInvoice(netto,bruto):
    if netto>bruto:
        raise ValueError("Netto can't be greater than bruto")
    else:
        print("The invoice has been processed")

def EndofMonth():
    netto=1230
    bruto=1000
    try:
        ProccessInvoice(netto,bruto)
    except ValueError as e:
        print("The values of inovices are incorrect: ",e)
        raise ValueError("The values of inovices are incorrect") from e
    except Exception as e:
        print("Error: ",e)
        raise Exception("Error") from e
try:
    EndofMonth()
except Exception as e:
    print("Error: ",e,e.__cause__)

    print("="*60)




print('='*60)
print('Assert')
import datetime as dt
netto=100
bruto=120
#netto must be less or equal to bruto
#assert netto<=bruto, "Netto can't be greater than bruto"




order_date=dt.date(2023,6,1)
delivery_date=dt.date(2023,5,1)
#order date must be earlier than delivery date
#assert order_date<delivery_date, "Order date can't be later than delivery date"





print('='*60)


print('MyException')

class BitException(Exception):
    def __init__(self, message,area):
        super().__init__(message)
        self.area=area
    def __str__(self):
        return "{} in area: {}".format(super().__str__(),self.area)

try:
    raise BitException("My exception no file","Finacial data")
except BitException as e:
    print("MyException: {} ".format(e))

class BitSecurityException(BitException):
    pass

class BitDataFormatException(BitException):
    pass   

try:
    raise BitSecurityException("Security error","Finacial data")
    
except BitSecurityException as e:
    print("Security error: ",e)
except BitDataFormatException as e:
    print("Data format error: ",e)
except BitException as e:
    print("MyException: ",e)
except Exception as e:
    print("Error: ",e)


print('='*60)  

import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
url = 'http://www.mobilo24.eu/spis'
dir = os.getcwd()+'/srednioZaawansowany'
tmpfile = 'download.tmp'
file = 'spis.html'
 
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
   # save_url_to_file(url, tmpfile_path)
    shutil.copy(tmpfile_path,file_path)
except requests.exceptions.ConnectionError as e:
    print("Connection failed url: {}".format(url),e)
except PermissionError as e:    
    print("Permission error 403",e)
except FileNotFoundError as e:
    print("File not found 404 ",e)
except Exception as e:
    print("Error",e)
else:
    print("Download completed")
finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    print("The end")
    print("="*60)


import datetime as dt
 
class Trip:
    

    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []
        for trip in trips:
            try:
                trip.check_data()
            except AssertionError as e:
                list_of_errors.append("Exception {}: {} ".format(trip.symbol,str(e)))
        assert len(list_of_errors) == 0, "The list of trips has errors: {}".format(list_of_errors)
        print("The offer will be published...")



    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        assert len(self.symbol) >0, "The symbol is empty!"
        assert self.start <= self.end, "The start date is later than the end date!"
 
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 1), dt.date(2023, 6, 12))
        ]

try:
    print("Start")
    Trip.publish_offer(trips)
    print("Done")
except Exception as e:
    print("Error: ",e)


    


