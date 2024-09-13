import time

class timeMeasure:
    def __init__(self):
        pass
    def __enter__(self):
        print('entering context')
        self.__start = time.time()
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.__end = time.time()
        self.__diff=self.__end-self.__start
        print('exiting context')
        print('Elapsed time:',self.__diff)

with timeMeasure():
    time.sleep(3)
    print('Inside context')

import os

class iniFile:
    def __init__(self,path):
        self.path=path
        self.parmeters={}
        self.readFromDisk()
    def readFromDisk(self):
        if os.path.isfile(self.path):
            with open(self.path) as file:
                for line in file:
                    if '=' in line:
                        key,value=line.rstrip('\n').split('=',1)
                        self.parmeters[key]=value
    def readParameter(self,key):
        return self.parmeters.get(key,None)
    def writeParameter(self,key,value): 
        self.parmeters[key]=value
    def saveOnDisk(self):
        with open(self.path,'w') as file:
            for key,value in self.parmeters.items():
                file.write(key+'='+value+'\n')
    def __enter__(self): 
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('exc_type:',exc_type)
        print('exc_val:',exc_val)
        print('exc_tb:',exc_tb)
        if exc_type== OSError:
            return False
        else:
            return True

path='srednioZaawansowany/config.ini'

'''
ini=iniFile(path)
ini.writeParameter('version','1.0')
ini.writeParameter('author','John Doe')
ini.saveOnDisk()

ini2=iniFile(path)
print(ini2.readParameter('version'))
print(ini2.readParameter('author'))
'''

with iniFile(path) as ini3:
    ini3.writeParameter('version','2.0')
    ini3.writeParameter('author','Jane Doe')
    ini3.saveOnDisk()
    print(ini3.readParameter('version'))
    print(ini3.readParameter('author'))

                
   


print('='*60)
print('Contextlib')


class Door:
    def __init__(self,where):
       self.where=where
    def open(self):
        print('Opening door to the {}'.format(self.where))
    def close(self):
        print('Closing door to the {}'.format(self.where))

from contextlib import contextmanager

@contextmanager
def openAndClose(door):
    door.open()
    yield door  
    door.close()

with openAndClose(Door('kitchen')) as door:
    print('Inside the block')


print('='*60)
from urllib.request import urlopen
from contextlib import closing  
with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        pass
    print('Page is closed')

print('='*60)

from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove('somefile.tmp')

print('='*60)
print(os.getcwd())
from contextlib import redirect_stdout
f=open(os.getcwd()+'/log.txt','a')
with redirect_stdout(f):
    print('This is written to the file')
    d=Door('garden')
    door.open()
    door.close()
f.close()
print('This is written to the console')
print('='*60)

import zipfile,os,requests

class FileFromWeb:
    def __init__(self,url,tmp_file):
        self.url=url
        self.tmp_file=tmp_file
    def __enter__(self):
        response=requests.get(self.url)
        with open(self.tmp_file,'wb') as file:
            file.write(response.content)
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_type==FileNotFoundError:
            print('File not found')
            return True
        elif exc_type==KeyError:
            print('File not found in the archive')
            return True
        else:
            return False


url='https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'  
tmp_file=os.path.join(os.getcwd()+'/srednioZaawansowany','eurofxref.zip')


with FileFromWeb(url,tmp_file) as f:
    with zipfile.ZipFile(f.tmp_file,'r') as z:
        a_file=z.namelist()[0]
        print(a_file)
        os.chdir(os.path.join(os.getcwd(),'srednioZaawansowany'))
        z.extract(a_file,'.',None)
print('='*60)   

class FileFromWeb:
 
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file
 
    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
 
    def close(self):
        #if os.path.isfile(self.tmp_file):
            os.remove(self.tmp_file)
 
import contextlib

with contextlib.suppress(FileNotFoundError):
    with contextlib.closing(FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'eurofxref.zip')) as f:
        f.download_file()
        with zipfile.ZipFile(f.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            z.extract(a_file, '.', None)
        os.remove(f.tmp_file)
    


    

        

        
