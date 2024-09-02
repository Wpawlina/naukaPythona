dayType=2

weekend=1
workday=2
holiday=3


if dayType==1:
    pass
elif dayType==2:
    pass
else:
    pass


dayDascription= 'Weekend' if dayType==1 else 'Workday' if dayType==2 else 'Holiday'
print('Weekend') if dayType==1 else print('Workday') if dayType==2 else print('Holiday')


price =123
bonus=23
bonus_granted=True
price=price-bonus if bonus_granted else price
print(price)

rating=5

print('very good') if rating==5 else print('good') if rating==4 else print('weak')

