import math
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
if len(inputdata)==len(factortable):
    minValue=float('inf')
    maxValue=-float('inf')
    for i in range(len(inputdata)):
        minValue=inputdata[i]-factortable[i]*inputdata[i]
        maxValue=inputdata[i]+factortable[i]*inputdata[i]
        print(minValue,maxValue)
        minInteger=math.floor(minValue)
        maxInteger=math.ceil(maxValue)
        print(minInteger,maxInteger)
else:
    import random
    minValue=float('inf')
    maxValue=-float('inf')
    for i in range(len(inputdata)):
        rand=random.random()
        minValue=inputdata[i]-rand*inputdata[i]
        maxValue=inputdata[i]+rand*inputdata[i]
        print(minValue,maxValue)
        minInteger=math.floor(minValue)
        maxInteger=math.ceil(maxValue)
        print(minInteger,maxInteger)
import datetime

print(datetime.datetime.today())
print(datetime.datetime.today().strftime('%Y-%m-%d'))
    
    
    