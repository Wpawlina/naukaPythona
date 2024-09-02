workDays=[19,21,22,21,20,22]
months=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']

monthDays=dict(zip(months,workDays))
print(monthDays)

for key in monthDays:
    print('Month:',key,'Work days:',monthDays[key])

for value in monthDays.values():
    print('Work days:',value)   

for key,value in monthDays.items():
    print('Month:',key,'Work days:',value)

for key in monthDays.keys():  
    print('Month:',key,'Work days:',monthDays[key])

print('===============================')


banknotes_coins=[0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,200,500]
dict_denominations={}
for value in banknotes_coins:
    dict_denominations[value]=0

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1 
 
dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2
 
dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for key in dict_denominations:
    print("Denomination: {:6.2f} Amount: {:5d}".format(float(key),int(dict_denominations[key])))




