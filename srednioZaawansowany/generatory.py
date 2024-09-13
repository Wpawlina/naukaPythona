import datetime as dt

def MillionDays(year,month,day,maxdays):
        date=dt.date(year,month,day)
        for i in range(maxdays):
            yield date
            date+=dt.timedelta(days=1)
         
for d in MillionDays(2000,1,1,3):
    print(d)
   
print('='*60)
def GetNumbers():
    yield(1)
    yield(22)
    yield(333)
    yield(4444)
    yield(55555)
    yield(666666)


r=GetNumbers()
a=next(r)
print(a)
print(next(r))
print(next(r))
print(next(r))

products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

def combination():
     for c in customers:
         for p in products:
             for pr in promotions:
                 yield (c,p,pr)
        
c=combination()
for i in range(12):
    cu,p,pr=next(c)
    print(cu,p,pr)



def getRecords(filePath):
     file=open(filePath)
     print('File open')
     for line in file:
          if ':' in line:
            type,action=line.rstrip('\n').split(':',1)
            record=(type,action)
            yield record
     print('File close')
     file.close()


for record in getRecords('srednioZaawansowany/data.txt'):
    print('Type:',record[0],'Action:',record[1])

import random

def random_with_sum(number_of_elements,asserted_sum):
    i=0
    print('Start',i)
    while True:
        i+=1
        elements=[random.randint(1,100) for _ in range(number_of_elements)]
        if sum(elements)==asserted_sum:
            yield (i,elements)
    

gen=random_with_sum(3,100)
for i in range(10):
    counter,elements=next(gen)
    print(counter,elements)
    

import os

path=os.getcwd()+'/srednioZaawansowany'
searchedString='Class'
file_extension='.py'




def generateFiles(path,file_extension):
    for dir_name,subdirs,files in os.walk(path):
        for file in files:
            if file.endswith(file_extension):
                file_path=os.path.join(dir_name,file)
                yield file_path

def grep(search,files):
    for file in files:
        with open(file) as file:
            for i,line in enumerate(file):
                if search in line:
                    yield file.name,i+1,line


files=generateFiles(path,'.py')
searched=grep('Class',files)
print(next(searched))
for file,line_number,line in searched:
    print('Found in file:',file,'line:',line_number,'line:',line)

import requests


dir=os.getcwd()+'/srednioZaawansowany/pages'  
def gen_get_files(dir):
    for file in os.listdir(dir):
        yield file
def gen_get_file_lines(file):
    with open(file) as file:
        for line in file:
            yield line.rstrip('\n')
def check_webpage(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        print('Webpage exists:',url)
    except Exception as e:
        print('Error:',str(e))
    
files=gen_get_files(dir)

for file in files:
    print('File:',file)
    lines=gen_get_file_lines(os.path.join(dir,file))
    for line in lines:
        check_webpage(line)






                        
    





