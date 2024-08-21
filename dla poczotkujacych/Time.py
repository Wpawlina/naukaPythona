import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

print(time.localtime(time.perf_counter()))#dokładnieszy czas pobrany z procesora

import calendar

print(calendar.month(2024,7,10,3))
print(calendar.weekday(2024,7,17))
calendar.setfirstweekday(6)
print(calendar.month(2024,7,10,3))
print(calendar.isleap(2024))
print(calendar.leapdays(2000,2025))
print(calendar.calendar(2024))

import datetime

print(datetime.MINYEAR,datetime.MAXYEAR)
dl=datetime.timedelta(days=1,hours=2,minutes=-30)
dl2=datetime.timedelta(days=-1,hours=-2,minutes=-3)
print(dl+dl2)


today=datetime.date.today()
daysToPay=datetime.timedelta(days=7)
print(today+daysToPay)
endOftheWorld=datetime.date.max
print(endOftheWorld)

born=datetime.date(2003,6,25)
print(today-born)
now=datetime.datetime.now()
print(now)
print(datetime.datetime.today())
print(datetime.datetime.utcnow())
print(datetime.datetime.today().weekday())

print(now.strftime("%Y-%m-%d %H:%M:%S:%f"))