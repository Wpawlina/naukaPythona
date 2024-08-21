age=12
isDrunk=True
isRestrictedArea=True

'''
if age >= 18 and not isDrunk and not isRestrictedArea:
    print('You are an adult and you can buy alkohol')
else:
    print("Sorry  we cannot sell you alkohol")
'''
if age<18:
    print('You are too young to buy alkohol')
elif isDrunk:
    print('You are drunk we cannot sell you alkolhol')
elif isRestrictedArea:
    print('This is restricted area, alkohol is forbidden')
else:
    print('OK, you can buy alkohol')




isPizzaOrdered=False
IsBigDrinkOrdered=False
isWeekend=False

if   isWeekend:
    print('PROMOCJA NIE OBOWIĄZUJE W WEEKENDY')
elif not IsBigDrinkOrdered and not isPizzaOrdered :
    print('MUSISZ ZAMÓWIĆ PIZZE LUB DUŻY NAPÓJ ABY SKORZYSTAĆ Z PROMOCJI')
else:
    print('OTRZYMUJESZ DARMOWEGO BURGERA')

itRains=False
print('we stay at home' if itRains else 'We go out')

musclePain=False
fever=False
weakness=True
isMan=True

if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print('suspision of influenza')
elif weakness and not fever and musclePain or weakness and not musclePain and fever:
    print('Just take a rest')
else:
    print('flu is unlikely')

isCheckCompleted=True
print('CHECK IS COMPLETED' if isCheckCompleted else 'NOT DONE YET!'  )




