from datetime import date
from datetime import timedelta
import geomod


def nextWorkingDay(year,month,day):
    day=date(year,month,day)
    if day.weekday()==5:
        workingday=day+timedelta(days=2)
    elif day.weekday()==6:
        workingday=day+timedelta(days=1)
    else:
        workingday=day
    return 'working day for '+ day.__str__() +' is ' +   workingday.__str__()
def howManyDaysUntilNewYear(*dates):
    for curDate in dates:  
        year=curDate.year
        endDate=date(year,12,31)
        dif=endDate-curDate
        print(dif.days)
def Weekday(dayNumber):
    names={
        0:'monday',
        1:'tuesday',
        2:'wednesday',
        3:'thursday',
        4:'friday',
        5:'saturday',
        6:'sunday'
    }
    return names.get(dayNumber,'error')




print(nextWorkingDay(2024,7,7))
howManyDaysUntilNewYear(date(2024,7,2),date(2024,6,25),date(2024,1,1),date(2024,11,11))
print(Weekday(2))
for i in range(1,11):
    print(geomod.giveGeomSeqElement(3,2,i))
print(geomod.giveFactorForGeomSeq(24,12))
print(geomod.giveSumOfNelementsGeomSeq(10,10,10))

