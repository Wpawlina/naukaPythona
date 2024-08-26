number=10
print('Variable number is:',number,id(number))
number+=2
print('Variable number is:',number,id(number))
print('===============================')

text='Hello World'
print('Variable text is:',text,id(text))
text+='!'
print('Variable text is:',text,id(text))
print('===============================')

list=[1,2,3]
print('Variable list is:',list,id(list))
list.append(4)
print('Variable list is:',list,id(list))
print('===============================')

list2=list
print('Variable list is:',list,id(list))
print('Variable list2 is:',list2,id(list2))
list2.append(5)
print('Variable list is:',list,id(list))
print('Variable list2 is:',list2,id(list2))
print('===============================')

list3=list.copy()
print('Variable list is:',list,id(list))
print('Variable list3 is:',list3,id(list3))
list3.append(6) 
print('Variable list is:',list,id(list))
print('Variable list3 is:',list3,id(list3))
print('===============================')

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
workdays=days.copy()
workdays.remove('Saturday')
workdays.remove('Sunday')
print('Variable days is:',days,id(days))
print('Variable workdays is:',workdays,id(workdays))
print('===============================')