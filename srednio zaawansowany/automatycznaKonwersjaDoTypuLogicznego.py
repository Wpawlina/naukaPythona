isOk=True
print('Variable isOk is:',isOk,type(isOk))
if isOk:
    print('True')  
print('===============================')
isOk='True'
print('Variable isOk is:',isOk,type(isOk))
if isOk:
    print('True')
print('===============================') 

isOk=0
print('Variable isOk is:',isOk,type(isOk))
if isOk:
    print('True')
print('===============================')
isOk=-1
print('Variable isOk is:',isOk,type(isOk))  
if isOk:
    print('True')
print('===============================')

list=[]
print('Variable list is:',list,type(list))  
if list:
    print('True')   
print('===============================')

list=[0,0,0]
print('Variable list is:',list,type(list))
if list:
    print('True')
print('===============================')


options=['load data','export data','analyze & predict']
choice='x'
while choice:
    print('Choose option:')
    for i in range(len(options)):
        print(f'{i+1}. {options[i]}')
    choice=input('Enter number:')
    try:
        choiceNum=int(choice)
        if choiceNum>0 and choiceNum<=len(options):
            print('You chose:',options[choiceNum-1])
        else:
            print('Wrong number')
    except :
        print('You must enter a number')

