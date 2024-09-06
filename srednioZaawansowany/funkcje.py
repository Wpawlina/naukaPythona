#wartosci domyślne
def buyMe(prefix='proszę o ', name='coś miłego'):
    print("Kup mi, " + prefix + name)

buyMe("proszę o ", "kawę")
buyMe(prefix="proszę o ", name="herbatę")
buyMe(name="herbatę", prefix="proszę o ")
buyMe("proszę o ")
buyMe(prefix="proszę o ")
buyMe(name="coś słodkiego")


def showProgress(howMany, character='*'):
    print(character * howMany)
showProgress(10)
showProgress(15)
showProgress(30)
 
showProgress(10, '-')
showProgress(15, '+')

#kwarg i args

def buyMe2(prefix='proszę o ', name='coś miłego',*args,**kwargs):
    print("Kup mi, " + prefix + name)
    print(args)
    print(*args)
    print(kwargs)

buyMe2("proszę o ", "kawę", "i", "herbatę",shop="sklep", shop2="sklep2")


products = ['mleko', 'ser', 'masło']
parmeter={'shop':'sklep', 'shop2':'sklep2'}
buyMe2("proszę o ", "kawę", *products, **parmeter)

def calculate_paint(efficency_ltr_per_m2, *rooms):
    paint_needed = 0
    for room in rooms:
        paint_needed += room
    return paint_needed * efficency_ltr_per_m2
print(calculate_paint(0.5, 100, 200, 300, 400))
rooms=[100, 200, 300, 400]
print(calculate_paint(0.5, *rooms))

import os
def logIt(*args):
    path = os.path.join(os.getcwd(), 'srednioZaawansowany\\log.txt')
    with open(path, 'a') as f:
        import datetime
        print(datetime.datetime.now(), file=f)
        for a in args:
            print(a, file=f)
        print('-'*40, file=f)

logIt('Starting processing forecasting')
logIt('ERROR', 'Not enough data', 'invoices', '2020')


#funkcja jako zmienna
print('funkcja jako zmienna')
stealForMe=buyMe

print(type(stealForMe))
stealForMe("proszę o ", "herbatę")

def goLeft(*args):
    print("W lewo z", *args)

def goRight(*args):
    print("W prawo z", *args)

def goForward(*args):
    print("Do przodu z", *args)    

def goBack(*args):
    print("Do tyłu z",*args)

def start(*args):
    print("Start z",*args)    

def stop(*args):
    print("Stop z",*args)

instructions = [start, goForward, goForward, goLeft, goForward, goRight, goForward, goForward, goBack, stop]

dish='pizza'
for ins in instructions:
    ins(dish)


def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2

number=8

instructions=[double, square, div2,negative]

tmp_return_value=number

for ins in instructions:    
    tmp_return_value=ins(tmp_return_value)
    print(tmp_return_value)

instructions=[square, square, div2,double]

tmp_return_value=number

for ins in instructions:    
    tmp_return_value=ins(tmp_return_value)
    print(tmp_return_value)

#funkcja jako argument funkcji
print('funkcja jako argument funkcji')


def Bake(what):
    print('Baking', what)

def Add(what):
    print('Adding', what)   

def Mix(what):
    print('Mixing', what)

cookbook = [(Add,'milk'), (Add,'eggs'),(Add,'flour'),(Add,'suger'),(Mix,'ingredients'),(Bake,'cake')]

for activity, obj in cookbook:
    activity(obj)

print('='*30)

def Cook(activity, obj):
    activity(obj)

Cook(Bake, 'bread')

for activity, obj in cookbook:
    Cook(activity, obj) 


# funkcje zwracające funkcje
print('funkcje zwracające funkcje')

def ceateFunction(kind='+'):
    source='''
def f(*args):
    result=0
    for a in args:
            result{}=a
    return result
'''.format(kind)
    exec(source,globals())
    return f

f_add=ceateFunction('+')    
f_sub=ceateFunction('-')    

print(f_add(1,2,3,4,5))
print(f_sub(1,2,3,4,5))

print('='*30)

import datetime
def createTimeDifFunction(step):
    source='''
def f(start, end):
    delta=end-start
    delta=delta.total_seconds()
    return delta/{}
'''.format(step)
    exec(source, globals())
    return f
f_seconds=createTimeDifFunction(1)
f_minutes=createTimeDifFunction(60)
f_hours=createTimeDifFunction(3600)

print(f_seconds(datetime.datetime(2020,1,1,0,0,0), datetime.datetime(2020,1,1,0,10,0)))
print(f_minutes(datetime.datetime(2020,1,1,0,0,0), datetime.datetime(2020,1,1,0,10,0)))
print(f_hours(datetime.datetime(2020,1,1,0,0,0), datetime.datetime(2020,1,1,0,10,0)))   


#wrrapper
print('wrapper')

def ChangeSalary(empName, newSalary,isBonus=False):
    print('Changing salary for', empName, 'to', newSalary,'as bonus',isBonus) 
    return newSalary

print(ChangeSalary('Johnson', 2000,True))


def createFunctionWithWrapper(func):
    def funcWithWrapper(*args, **kwargs):
        print('Function ',func.__name__ ,' started at ', datetime.datetime.now().isoformat())
        print('Following arguments were used:', args, kwargs)
        result=func(*args, **kwargs)
        print('Function returned ', result)
        return result
    return funcWithWrapper
ChangeSalaryWithLog=createFunctionWithWrapper(ChangeSalary)
print(ChangeSalaryWithLog('Johnson', 2000,True))


@createFunctionWithWrapper
def ChangeSalary(empName, newSalary,isBonus=False):
    print('Changing salary for', empName, 'to', newSalary,'as bonus',isBonus) 
    return newSalary

print(ChangeSalaryWithLog('Johnson', 1000,True))

def createTimeWrapper(func):
    def functionWithWrapper(*args, **kwargs):
        start=datetime.datetime.now()
        result=func(*args, **kwargs)
        stop=datetime.datetime.now()
        print('Function ',func.__name__ ,' lasted ', stop-start,'seconds')
        return result
    return functionWithWrapper



@createTimeWrapper
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v
    
print(get_sequence(2))

#wrapper z argumentami
print('wrapper z argumentami')


def createFunctionWithWrapperAndArguments(logFilePath):
    def createFunctionWithWrapper(func):
        def fun_with_wrapper(*args, **kwargs):
            file=open(logFilePath, 'a')
            file.write('='*30+'\n')
            file.write('Function '+func.__name__+' started at '+datetime.datetime.now().isoformat()+'\n')
            file.write('Following arguments were used \n')
            file.write(" ".join('{}'.format(a) for a in args)+'\n')
            file.write(" ".join('{}={}'.format(k,v) for k,v in kwargs.items())+'\n')
            result=func(*args, **kwargs)
            file.write('Function returned '+str(result)+'\n')
        
            file.close()
            return result
        return fun_with_wrapper
    return createFunctionWithWrapper



        
   
    
@createFunctionWithWrapperAndArguments(os.path.join(os.getcwd(), 'srednioZaawansowany\\log.txt'))
def ChangeSalary(empName, newSalary,isBonus=False):
    print('Changing salary for', empName, 'to', newSalary,'as bonus',isBonus) 
    return newSalary

print(ChangeSalary('Johnson', 3000,True))


import os

def createFunctionWithWrapperAndArguments(logFilePath):
    def createFunctionWithWrapper(func):
        def fun_with_wrapper(path):
            file=open(logFilePath, 'a')
            file.write('='*30+'\n')
            file.write('Function '+func.__name__+' executed on '+path+' '+datetime.datetime.now().isoformat()+'\n')
            result=func(path)
            file.close()
            return result
        return fun_with_wrapper
    return createFunctionWithWrapper


        
@createFunctionWithWrapperAndArguments(os.path.join(os.getcwd(), 'srednioZaawansowany\\log.txt'))
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")
@createFunctionWithWrapperAndArguments(os.path.join(os.getcwd(), 'srednioZaawansowany\\log.txt'))
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)

create_file(os.path.join(os.getcwd(), 'srednioZaawansowany\\test3.txt'))
delete_file(os.path.join(os.getcwd(), 'srednioZaawansowany\\test3.txt'))


   